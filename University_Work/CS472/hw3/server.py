#!/usr/bin/env python3

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

class FTPSession:
    def __init__(self, clientsocket, address, port):
        self.clientsocket = clientsocket
        self.address = address
        self.aport = port
        self.clientAddress = "[%s:%s]"%(self.address, self.aport)

        self.username = ""
        self.passwd = ""
        self.state = STATE.UNAUTHOTHORIZED

        self.datasocket = None
        self.dataport = 20

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
        The main loop that clients exist in, this is where a user will interact with the server,
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
        Function the sends messages to the client, note we also log to the logger here aswell
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
        Function that handles requires a second socket to send data
        """
        response = ""
        try:
            if self.state == STATE.PASSIVE: #state is passive
                (dsocket, self.address) = self.datasocket.accept()
            else:
                dsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                dsocket.connect( (socket.gethostname(), self.dataport) )

            for value in values:
                dsocket.send( (str(value) + "\r\n").encode() )

            dsocket.close()

            # leave massive mode
            if self.state == STATE.PASSIVE: #state is passive
                self.state = STATE.IDLE
                self.datasocket.close()

            response = "226 Closing data connection."
        except socket.error as e:
            log.elog("DATASOCKET SEND" + str(e))
            response = "425 Can't open dataconnection"

        return response

    def datasocketrecv(self):

        response = ""
        recvd = ""
        try:
            if self.state == STATE.PASSIVE: #state is passive
                (dsocket, self.address) = self.datasocket.accept()
            else:
                dsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                dsocket.connect( (socket.gethostname(), self.dataport) )

            while True:
                message = dsocket.recv(BUFFER).decode()
                recvd += message
                print("message:",message, "message len:", len(message))
                if not message:
                    break

            if self.state == STATE.PASSIVE: #state is passive
                self.state = STATE.IDLE
                self.datasocket.close()
            response = "226 Closing data connection."
        
        except socket.error as e:
            log.elog("DATASOCKET RECV " + str(e))
            response = "425 Can't open dataconnection"
        
        return (response, recvd)


    def pasv(self, cmd):
        """         
        Puts client into passive mode, and retrieve the..
        """
        try:
            hostname = socket.gethostname()
            (hostname, _, hostip) = socket.gethsotbyaddr(hostname)
            host = hostip[0].replace(".", ",")

            # TODO put into passive mode

            self.state = STATE.PASSIVE

            with lock:
                self.datasocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.datasocket.bind( (hostname, 0) )
                self.datasocket.listen(5)

            self.dataport = self.datasocket.getsockname()[1]
            remainderport = self.dataport % 256

            p1 = (self.dataport - remainderport) / 256
            p2 = remainderport

            print("PASV REACHED")

            command = "277 Entering Passive Mode (%s,%s,%s)."%(host,p1,p2)
        except Exception as e:
            command = "501 Passive Mode Broke"
            log.elog("Error in PASSIVE " + str(e))
        self.send(command)

    def port(self, cmd):
        """
        Function to handle port requests
        """
        try:
            msg = ''.join(cmd)
            pasv = msg[4:].translate({ord(c): None for c in '().\r\n'}).split(",")
            print(pasv)
            p1 = int(pasv[-2])
            p2 = int(pasv[-1])

            port = (p1 * 256) + p2

            if port < 0 or port > 65535:
                raise Exception("Received port out of range " + port)

            self.dataport = port

            self.state = STATE.IDLE
            command = "200 Port okay."

        except Exception as e:
            log.elog("ERROR in PORT " + str(e))
            command = "501 Syntax error in parameters or arguments."

        self.send(command)

    def welcome(self):
        """
        The intro message to the FTP Client, so it knows it connected
        """
        message = "220 Welcome to the Server" 
        self.send(message)

    def close(self):
        self.send("421 Remote Host has Closed")
        self.clientsocket.shutdown(socket.SHUT_WR)

    def CMD_lookup(self, cmd):
        return {
            "USER" : (self.user),
            "PASS" : (self.password),
            "SYST" : (self.syst),
            "PORT" : (self.port),
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
        Quit the operation
        """
        command = "221 Goodbye."
        self.send(command)
        self.clientsocket.shutdown(socket.SHUT_WR)

    def user(self, response):

        # TODO check args

        self.username = response[1]
        self.send("331 Please specify the password.")

    def password(self, response):

        # TODO check args

        self.passwd = response[1]

        if self.authenticate(self.passwd):
            command = "230 Login Successful"
            self.state = STATE.IDLE
        else:
            command = "530 Incorrect Credentials"

        self.send(command)

    def authenticate(self, passwd):
        return self.username == "cs472" and "hw3" == passwd

    def notAuthorized(self):
        if self.state == STATE.UNAUTHOTHORIZED:
            self.send("530 Login incorrect")
            return True
        return False

    def noArguements(self, cmd):
        if len(cmd) == 1:
            self.send("501 Not enough arguements given")
            return True
        return False

    def syst(self, response):

        if self.notAuthorized():
            return

        system = sys.platform
        command = "215 UNIX Type: %s"%system
        self.send(command)

    def list(self, response):

        if self.notAuthorized():
            return
        
        dirlist = os.listdir(os.getcwd())
        command = "150 File status okay; about to open data connection."
        self.send(command)

        command = self.datasocketsend(dirlist)
        self.send(command)

    def pwd(self, cmd):

        if self.notAuthorized():
            return

        message = "257 %s" % os.getcwd()
        self.send(message)

    def cwd(self, cmd):

        if self.notAuthorized():
            return

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

        if self.notAuthorized():
            return

        message = "250 Requesting file action okay, completed."
        newloc = os.getcwd() + "/.."
        os.chdir(newloc)

        self.send(message)

    def stor(self, cmd):

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

class ServerSocket:

    def __init__(self, port, backlog = 5):
        self.port = int(port)
        self.backlog = int(backlog)

        self.host = socket.gethostname()

        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind( (socket.gethostbyname(self.host), self.port) )
        self.serversocket.listen(self.backlog)
        print(socket.gethostbyname(self.host), self.port)

    def accept(self):
        return self.serversocket.accept()
    
    def close(self):
        return self.serversocket.close()

class Logger:
    
    def __init__(self, filename):
        self.filename = filename
        self.format = "%Y-%m-%d %H:%M"
        self.file = open(self.filename, "w+")

    def close(self):
        self.file.close()

    def sending(self, message, clientAddress):
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


def main():
    
    global log
    ftpserver = None

    # check cli arguments, and setup socket
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        port = sys.argv[2]

    else:
        print("Incorrect Usage: servery.py <filename> <port>")
        exit(2)

    log = Logger(filename)
    serversocket = ServerSocket(port)

    # While each client connects, each client uses a seperate thread
    print("reached")
    while True:
        try:
            print("waiting for accept v2")
            (clientsocket, address) = serversocket.accept()
            print("accepted")
            ftp = FTPSession(clientsocket, address[0], address[1])
            ftp.startSession()
        except:
            log.close()
            if ftpserver:
                ftpserver.close()
            serversocket.close()
            print("Ended Sessions")
            if ftpserver:
                ftpserver.close()
            # You might have to keep track of all sessions
            exit(3)

if __name__ == "__main__":
    main()
