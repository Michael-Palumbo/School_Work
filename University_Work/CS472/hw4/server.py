#!/usr/bin/env python3

#UPDATED

import socket
import sys
import threading
import os
import datetime

log = None
BUFFER = 1024
lock = threading.Lock()

class STATE:
    """
    Class that acts like an ENUM, all associated values are abstract and 
    are used for uniqueness between states
    """
    UNAUTHOTHORIZED = 0
    IDLE = 1
    PASSIVE = 2
    CONNECTED_IDLE = 3
    CONNECTED_PASSIVE = 4
    def connected(num):
        return num == STATE.CONNECTED_PASSIVE or STATE.CONNECTED_IDLE

class FTPSession:
    """
    Class that serves as the main interface for the client. 
    Args:
        clientsocket = reference to the client's socket
        address = reference to the ip of the client
        port = reference to the port of the client
        clientAddress = userd to easy format the address and ip for logging
        username = the inputed username from the client
        passwd = the inputed password fromt he client
        datasocket = the secondary socket used to send data between the user and server
        dataport = the port that the datascoket will use to send data (default is 20)
    """
    COMMENT_SYMBOL = "#"
    CONFIG_VARIABLES = {"port_mode":False, "pasv_mode":False}
    
    def __init__(self, clientsocket, address, port, cred_filename):
        self.clientsocket = clientsocket
        self.address = address
        self.aport = port
        self.clientAddress = "[%s:%s]"%(self.address, self.aport)

        self.username = ""
        self.passwd = ""
        (self.valid_username, self.valid_password) = self.get_credetials(cred_filename)

        self.state = STATE.UNAUTHOTHORIZED


        self.datasocket = None
        self.dataport = 20


    def get_credetials(self, filename):
        """
        Helper function to grab the credentails from a file provided
        Note that the credentials is very minimal, first line is username,
        second line is password
        """
        with open(filename, "r") as f:
                valid_username = f.readline().strip()
                valid_password = f.readline().strip()
        return valid_username, valid_password



    def startSession(self):
        """
        Starts the client on a new thread, and moves them to the self.session() function, 
        the main thread returns with a reference to the client's thread 
        """
        thread = threading.Thread( target = self.session )
        thread.daemon = True
        thread.start()
        return thread
        
    def session(self):
        """ 
        The main loop that a client exists in, this is where a user will interact with the server,
        each connected client exists in their own FTPSession
        """

        self.welcome() # Since ftp requires recieving a message first
        
        while True:
            try: 
                response = self.recv()
                splitResponse = response.split()
                function = self.CMD_lookup(splitResponse[0])
                function(splitResponse)
            except socket.error as e:
                log.elog("SESSION ERROR " + str(e))


    def send(self, message):
        """
        Function that sends messages to the client, note we also log to the logger here aswell
        """
        try:
            log.sending(message, self.clientAddress)
            message += "\r\n" # messages must end in the return and new line escape character
            self.clientsocket.sendall(str.encode(message))

        except socket.error as e:
            log.elog("Error on SEND: " + str(e))

    def recv(self):
        """
        Function to recieve messages from the client
        """
        response = ""
        while True:
            try:
                self.clientsocket.settimeout(1)
                mess = self.clientsocket.recv(BUFFER).decode()
                #print("mess is of type", type(mess))
                response += mess
                if '\n' in mess:
                    break
            except socket.timeout:
                continue
            except Exception as e:
                log.elog("Error on RECV: " + str(e))
        log.receiving(response, self.clientAddress)
        return response

    def datasocketsend(self, values):
        """
        Function that handles sending data on the client via a secondary socket, aka the data socket
        values: value is usually a massive string of whatever data needs to be sent over
        """
        response = ""
        try:
            if self.state == STATE.CONNECTED_PASSIVE: #state is passive
                (dsocket, self.address) = self.datasocket.accept()
            elif self.state == STATE.CONNECTED_IDLE:
                dsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                dsocket.connect( (socket.gethostname(), self.dataport) )
            # else:
            #     self.send("400 not connected, try using PORT")
            #     return 

            for value in values:
                dsocket.send( (str(value) + "\r\n").encode() )

            dsocket.close()

            if self.state == STATE.CONNECTED_PASSIVE: #state is passive
                self.datasocket.close()

            self.state = STATE.IDLE

            response = "226 Closing data connection."
        except socket.error as e:
            log.elog("DATASOCKET SEND" + str(e))
            response = "425 Can't open dataconnection"

        return response

    def datasocketrecv(self):
        """
        Function that handles recieving data on the client via a secondary socket, aka the data socket
        returns: 
            response: the command that the server is responding with
            recd: the information that has been recieved on the second socket
        """
        response = ""
        recvd = ""
        try:
            if self.state == STATE.CONNECTED_PASSIVE: #state is passive
                (dsocket, self.address) = self.datasocket.accept()
            elif self.state == STATE.CONNECTED_IDLE:
                dsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                dsocket.connect( (socket.gethostname(), self.dataport) )
            else:
                self.send("400 not connected, try using PORT")
                return "", "Something went wrong"

            while True:
                message = dsocket.recv(BUFFER).decode()
                recvd += message
                print("message:",message, "message len:", len(message))
                if not message:
                    break

            if self.state == STATE.CONNECTED_PASSIVE: #state is passive
                self.datasocket.close()

            self.state = STATE.IDLE

            response = "226 Closing data connection."
        
        except socket.error as e:
            log.elog("DATASOCKET RECV " + str(e))
            response = "425 Can't open dataconnection"
            recvd = "Something went wrong"
        
        return (response, recvd)


    def pasv(self, cmd):
        """         
        Puts the client into passive mode, and preps the client with the ips
        """

        if self.notAuthorized():
            return

        if not FTPSession.CONFIG_VARIABLES["pasv_mode"]:
            self.send("502 The command was not accepted, pasv mode not enabled")
            return

        message = ""
        try:
            hostname = socket.gethostname()
            (hostname, _, hostip) = socket.gethostbyaddr(hostname)
            host = hostip[0].replace(".", ",")

            # TODO put into passive mode

            self.state = STATE.CONNECTED_PASSIVE

            with lock:
                self.datasocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.datasocket.bind( (hostname, 0) )
                self.datasocket.listen(5)

            self.dataport = self.datasocket.getsockname()[1]
            remainderport = self.dataport % 256

            p1 = (self.dataport - remainderport) // 256
            p2 = remainderport

            message = "277 Entering Passive Mode (%s,%s,%s)."%(host,p2,p1)
        except Exception as e:
            message = "501 Unable to connect passive mode"
            log.elog("Error in PASSIVE " + str(e))
        self.send(message)

    def epsv(self, cmd):
        """
        Extended Passive function
        """

        if self.notAuthorized():
            return

        if not FTPSession.CONFIG_VARIABLES["pasv_mode"]:
            self.send("502 The command was not accepted, pasv mode not enabled")
            return

        message = ""
        try:
            hostname = socket.gethostname()
            (hostname, _, hostip) = socket.gethostbyaddr(hostname)

            self.STATE = STATE.CONNECTED_PASSIVE

            with lock:
                self.datasocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.datasocket.bind( (hostname, 0) )
                self.datasocket.listen(5)

            self.dataport = self.datasocket.getsockname()[1]

            message = "229 Entering Passive Mode (|||%s)."%(self.dataport)
        except Exception as e:
            message = "501 Unable to connect extended passive mode"
            log.elog("Error in PASSIVE " + str(e))
        
        self.send(message)

    def port(self, cmd):
        """
        Port Function to handle port requests
        """

        if self.notAuthorized():
            return

        if not FTPSession.CONFIG_VARIABLES["port_mode"]:
            self.send("502 The command was not accepted, port mode not enabled")
            return

        message = ""
        try:
            msg = ''.join(cmd)
            addi = msg[4:].translate({ord(c): None for c in '().\r\n'}).split(",")

            p1 = int(addi[-2])
            p2 = int(addi[-1])

            port = (p1 * 256) + p2

            if port < 0 or port > 65535:
                raise Exception("Received port out of range " + port)

            self.dataport = port

            self.state = STATE.CONNECTED_IDLE
            message = "200 Port okay."

        except Exception as e:
            log.elog("ERROR in PORT " + str(e))
            message = "501 Syntax error in parameters or arguments."

        self.send(message)

    def eprt(self, cmd):
        """
        Extended Port Function to handle eprt requests
        """

        if self.notAuthorized():
            return

        if not FTPSession.CONFIG_VARIABLES["port_mode"]:
            self.send("502 The command was not accepted, port mode not enabled")
            return

        message = ""
        try:
            addi = cmd[1]
            addi = addi[1:-1]

            _, _, port = addi.split("|")

            self.dataport = int(port)

            self.state = STATE.CONNECTED_IDLE
            message = "200 Port okay."
        except Exception as e:
            log.elog("ERROR in PORT " + str(e))
            message = "501 Syntax error in parameters or arguments."

        return self.send(message)

    def welcome(self):
        """
        The intro message to the FTP Client, so it knows it connected
        """
        message = "220 Welcome to the Server" 
        self.send(message)

    def close(self):
        """
        Function to close close the client's socket
        """
        self.send("421 Remote Host has Closed")
        self.clientsocket.shutdown(socket.SHUT_WR)

    def CMD_lookup(self, cmd):
        """"
        Function that handles a looopup for every command that a client can do
        cmd = the command, the first word that client typed
        return: reference to the function that matches the given command
        """
        return {
            "USER" : (self.user),
            "PASS" : (self.password),
            "SYST" : (self.syst),
            "PASV" : (self.pasv),
            "EPSV" : (self.epsv),
            "PORT" : (self.port),
            "EPRT" : (self.eprt),
            "LIST" : (self.list),
            "QUIT" : (self.quit),
            "PWD" : (self.pwd),
            "CDUP" : (self.cdup),
            "RETR" : (self.retr),
            "STOR" : (self.stor),
            "CWD" : (self.cwd),
            }.get(cmd, (self.invalid))

    def invalid(self, cmd):
        """
        USER input a command that could not be recognized
        """
        message = "400 \"%s\" was an invalid command"%(cmd)
        self.send(message)

    def quit(self, cmd):
        """
        Quit the connection
        """
        message = "221 Goodbye."
        self.send(message)
        self.clientsocket.shutdown(socket.SHUT_WR)

    def user(self, response):
        """
        Function to handle the inputted username, and then request for the password
        response: an array of words that the client sent
        """
        if self.noArguements(response):
            return

        self.username = response[1]
        self.send("331 Please specify the password.")

    def password(self, response):
        """
        Function to handle the inputted password, and then check whether the match with the server's client credentials
        response: an array of words that the client sent
        """
        message = ""
        if self.noArguements(response):
            return

        self.passwd = response[1]

        if self.authenticate():
            message = "230 Login Successful"
            self.state = STATE.IDLE
        else:
            message = "530 Incorrect Credentials"

        self.send(message)

    def authenticate(self):
        """
        Function to quickly check if clients username and password matches the server's client credentials
        returns: a boolean of whether it matched or not
        """
        return self.username == self.valid_username and self.valid_password == self.passwd

    def notAuthorized(self):
        """
        A helper function to quickly determine if the user is in the authenticated state
        returns: true whether the user is NOT authorized
        """
        if self.state == STATE.UNAUTHOTHORIZED:
            self.send("530 Login incorrect")
            return True
        return False

    def noArguements(self, cmd):
        """
        A helper function to quickly determine if the user has arguements occampying the command
        returns: true if no arguements were given to the function
        """
        if len(cmd) == 1:
            self.send("501 Not enough arguements given")
            return True
        return False

    def syst(self, response):
        """
        Function that handles the "sys" command, simply prints out the system's operating system
        """
        if self.notAuthorized():
            return

        system = sys.platform
        message = "215 UNIX Type: %s"%system
        self.send(message)

    def list(self, response):
        """
        Function to list out server's files and directories, we send this list on the data socket so files aren't interpretted as commands
        """
        if self.notAuthorized():
            return
        
        dirlist = os.listdir(os.getcwd())
        message = "150 File status okay; about to open data connection."
        self.send(message)

        message = self.datasocketsend(dirlist)
        self.send(message)

    def pwd(self, cmd):
        """
        Function to print out the current working directory to the client
        """
        if self.notAuthorized():
            return

        message = "257 %s" % os.getcwd()
        self.send(message)

    def cwd(self, cmd):
        """
        Function to change directories
        """
        if self.notAuthorized():
            return

        message = ""

        newloc = cmd[1]
        if newloc[0] != "/":
            newloc = os.getcwd() + "/" + newloc

        if os.path.isdir(newloc):
            os.chdir(newloc)
            message = "250 Requested file action completed"
        else:
            message = "550 Requested action not taken"
        self.send(message)

    def cdup(self, cmd):
        """
        Function to move one space up in a directory
        """
        if self.notAuthorized():
            return

        message = "250 Requesting file action okay, completed."
        newloc = os.getcwd() + "/.."
        os.chdir(newloc)

        self.send(message)

    def stor(self, cmd):
        """
        Function to store the file given by the user. The file's contents is send through the data socket
        cmd = and array of words that the user gave. ex: ["STOR", "file_a.txt"]
        """

        if self.notAuthorized() or self.noArguements(cmd):
            return

        filepath = cmd[1]

        try:
            file=open(filepath, "w+")

            message = "150 File status okay, openning data connection"
            self.send(message)

            response, data = self.datasocketrecv()
            file.write(data)
            file.close()

            self.send(response)

        except IOError as e:
            log.elog("Error in STOR " + str(e))
            message = "550 Requested action not taken"
            self.send(message)

    def retr(self, cmd):
        """
        Function to send the file to the client. The file's contents is send through the data socket
        cmd = and array of words that the user gave. ex: ["RETR", "file_a.txt"]
        """
        if self.notAuthorized() or self.noArguements(cmd):
            return

        filepath = cmd[1]
        content = ""

        try:
            with open(filepath, "r") as f:
                content = f.read()
            
            message = "150 File status okay; about to open data connection"
            self.send(message)

            listedData = []
            listedData.append(content)

            message = self.datasocketsend(listedData)
            self.send(message)

        except IOError as e:
            log.elog("Error in RETR " + str(e))
            message = "550 Requested action not taken"
            self.send(message)

class Logger:
    """
    Class that keeps track of logging all sending and recieving messages between the server and the client
    Args:
        filename = the file that the contents of the log will be saved
        format = the format inwhich we will record the year, month, hours and minutes
        file = the file object that we will write to
    """
    def __init__(self, filename):
        self.filename = filename
        self.format = "%d-%m-%Y %H:%M:%S"
        self.file = open(self.filename, "w+")

    def close(self):
        self.file.close()

    def sending(self, message, clientAddress):
        # print("Writing: " )
        self.file.write(str(self.get_time()) + " Sending to " + clientAddress + ": " + message.strip() + "\n")

    def receiving(self, message, clientAddress):
        self.file.write(str(self.get_time()) + " Recieving from " + clientAddress + ": " + message.strip() + "\n")

    def log(self, message):
        print(message)

    def elog(self, message):
        print(message, file=sys.stderr)

    def get_time(self):
        timenow = datetime.datetime.now()
        return timenow.strftime(self.format)

#NEW_INFO

def get_variables(all_text):
    """
    With the text of the given input file, i look through the lines,
    make sure none are a comment, and then assign the value if it exists
    """
    for line in all_text:
        if line[0] != FTPSession.COMMENT_SYMBOL and len(line) > 2:
            get_variable(line)

def get_variable(line):
    words = line.split()
    if words[0] in FTPSession.CONFIG_VARIABLES.keys():
        FTPSession.CONFIG_VARIABLES[words[0]] = value_to_bool(words[2])

def value_to_bool(value):
    return value == 'true'


def main():
	"""
	Main function. First we check arguements, then we set up the socket that the server that will manage connections.
	We then loop for each connecting client, when a client connects, we put them on a new thread, that new thread
	runs through the ftpSession's session() function, and the main threaad returns here waiting for a new connection.
	"""
	global log
	ftpserver = None

	# check cli arguments, and setup socket
	if len(sys.argv) == 3:
		filename = sys.argv[1]
		port = int(sys.argv[2])

	else:
		print("Incorrect Usage: servery.py <filename> <port>")
		exit(2)

	log = Logger(filename)
	# serversocket = ServerSocket(port)

	host = socket.gethostname()

	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.bind( (socket.gethostbyname(host), port) )
	serversocket.listen(5)
    
	print("Server openned on", socket.gethostbyname(host), port)

	with open("ftpserverd.conf", "r") as conf:
		get_variables(conf.readlines())

    #NEW_INFO
	if not FTPSession.CONFIG_VARIABLES["port_mode"] and not FTPSession.CONFIG_VARIABLES["pasv_mode"]:
		print("ERROR: Cannot have both port_mode and pasv_mode false")
		exit(1)

	print(f'port_mode = {FTPSession.CONFIG_VARIABLES["port_mode"]}')
	print(f'pasv_mode = {FTPSession.CONFIG_VARIABLES["pasv_mode"]}')

	# While each client connects, each client uses a seperate thread
	while True:
		try:
			(clientsocket, address) = serversocket.accept()
			ftp = FTPSession(clientsocket, address[0], address[1], "credentials")
			ftp.startSession()
		except KeyboardInterrupt as e:
			print("MAIN RETURN: " + str(e))
			log.close()
			if ftpserver:
				ftpserver.close()
			serversocket.close()
			print("Ended Sessions")
			if ftpserver:
				ftpserver.close()
			exit(3)

if __name__ == "__main__":
	main()
