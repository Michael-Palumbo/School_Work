#!/usr/bin/env python
import socket 
import sys
import threading
import os

#import configparser to read from config file
from configparser import ConfigParser, DuplicateOptionError, Error

#logger class
from logging import logger


#read from config file
authorized_users_file = "users.ini"
config = ConfigParser()

#Global Variables
BUFFER = 1024
AUTHORIZED_USERS = {}
log = None
lock = threading.Lock()
connected = True

"""
TODO:
	fix ls command
"""


class FTPServer(threading.Thread):
	"""
	FTPServer handles managing the connections and status response from the clients
	Attributes:
		socket: clientsocket
		address: clientsocket address
		path: the current os path of the server
		username: the username of the client
		password: the password of the client
		__authenticated: boolean to check if the user is authenticated or not
		dataport: the port of the datasocket
		passivemode: boolean to check if in passive mode or not
		passivesocket: the passivesocket if in passive mode
	"""

	def __init__(self, socket, address=None):
		self.socket = socket
		self.address = address
		self.path = os.getcwd()
		self.connect = True
		self.username = None
		self.password = None
		self.__authenticated = False
		self.dataport = 20 #default 20
		self.passivemode = False
		self.passivesocket = None
		self.client="[%s:%s]" %(address[0], address[1])


	def _authentication(function):
		"""
		Decorator function to handle if user is authenticated or not
		:param function: the function that requires authentication
		:return: returns the function or returns nothing
		"""
		def authwrapper(self, *args):
			if not self.__authenticated:
				command = "530 Login incorrect."
				self.send(command)
				return
			return function(self, *args)
		return authwrapper



	def _argumentrequired(function):
		"""
		Decorator function to handle if an argument is required for that function
		:param function: the function that requires an argument eg {CD <argument>}
		:return: returns the function or returns nothing
		"""
		def argumentwrapper(self, *args):
			#If I am exptecting an argument dont waste my time if not just return invalid syntax
			if len(*args) != 2:
				command = "501 Syntax error in parameters or arguments. Need an argument"
				self.send(command)
				return
			return function(self, *args)
		return argumentwrapper


	def _noarguments(function):
		"""
		Decorator function to handle a function that has no arguments
		:param function: the function that requires no arguments eg if you send me {QUIT asdasd}, returning a 501
		:return: returns the function or returns nothing
		"""
		def noargswrapper(self, *args):
			#I am expecting only one argument if you send me other info, getting a 501
			if len(*args) != 1:
				command = "501 Syntax error in parameters or arguments. No arguments in request"
				self.send(command)
				return
			return function(self, *args)
		return noargswrapper


	def _thread(function):
		"""
		Decorator function to handle if an argument is required for that function
		:param function: the function that requires an argument eg {CD <argument>}
		:return: returns the function or returns nothing
		"""
		def threadwrapper(self, *args):
			thread = threading.Thread(target=function, args=(self, ))
			thread.start()

		return threadwrapper


	@_thread
	def doProtocol(self):
		"""
		Function that will run the FTP protocol threaded and continuously
		:return: returns nothing
		"""
		self.welcome()
		while self.connect:
			try:
				message = self.receive()
				if message:
					log.received(message, self.client)
					parsedmessage = message.split()
					(function, cmd) = self.evaluation(parsedmessage[0], parsedmessage)
					function(cmd)
				elif not connected:
					break
			except socket.error as error:
				msg = "Client Disconneted %s" %self.client
				log.debug(msg)
				break


	def receive(self):
		"""
		Function that will receive messages from the client socket and return the message
		:return: returns the messages received from the socket
		"""
		response = ""
		while True:
			try:
				if connected:
					self.socket.settimeout(1)
					message = self.socket.recv(BUFFER)
					response += message
					if '\n' in message:
						break
				else:
					break

			except socket.timeout:
				#catch the timeout error
				continue #continue reading from the socket until we get something

			except Exception as error:
				log.error("RECV " + str(error))
				break

		return response


	def send(self, command=None):
		"""
		Send function that will send the command to the client socket
		:param command: the command from the server to send to the client
		:return: returns nothing
		"""
		try:
			command+="\r\n"
			log.sending(command, self.client)
			self.socket.sendall(command)

		except socket.error as error:
			log.error(str(error), self.client)


	def datasocket(self, command=None):
		"""
		Function that handles sending data on the datasocket for active and passive mode
		:param command: the command from the server to send to the client
		:return: returns the response of the status of the data transfer
		"""
		response = "425 Can't open dataconnection"
		try:
			dsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			if self.passivemode:
				(dsocket, self.address) = self.passivesocket.accept()
			else:
				dsocket.connect((socket.gethostname(), self.dataport))

			for value in command:
				dsocket.send(str(value) + "\r\n")

			#close the datasocket
			dsocket.close()

			#if we were in passive mode close the passive socket
			if self.passivemode:
				self.passivesocket.close()

			response = "226 Closing data connection. Requested file action successful"

		except socket.error as error:
			log.error("datasocket " + str(error), self.client)
			print("port: %s host: %s" %(self.dataport, socket.gethostname()))

		return response



	def datasocketrecv(self):
		"""
		Function that handles receiving data on the datasocket for active and passive mode
		:return: returns the response of the status of the data transfer, and the data received from the datasocket
		"""
		response = "425 Can't open dataconnection"
		recvdata = ""
		try:
			dsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			if self.passivemode:
				(dsocket, self.address) = self.passivesocket.accept()
			else:
				dsocket.connect((socket.gethostname(), self.dataport))

			while True:
				message = dsocket.recv(BUFFER)
				recvdata += message
				if '\n' in message:
					break

			if self.passivemode:
				self.passivesocket.close()

			response = "226 Closing data connection. Requested file action successful"

		except socket.error as error:
			pass

		return (response, recvdata)



	def welcome(self):
		"""
		Welcome function that sends the welcome message to the clientsocket
		:return: returns nothing
		"""
		command = "220 Service ready for new user."
		self.send(command)


	def close(self):
		"""
		Close function is called when the server is shutting down, changes connect variables to stop threads
		:return: returns nothing
		"""
		global connected
		connected = False
		self.connect = False
		#if socket still exists
		if self.socket:
			command = "421 Service not available, remote server has closed connection"
			self.send(command)
			self.socket.shutdown(socket.SHUT_WR)


	@_argumentrequired
	def user(self, cmd):
		"""
		User function to handle request made with user command
		:decorator _argumentrequired: argument is required for this function
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""
		self.username = cmd[1]
		command = "331 Please specify the password."

		self.send(command)

	@_argumentrequired
	def passwd(self, cmd):
		"""
		Password function to handle request made with the pass command
		:decorator _argumentrequired: argument is required for this function
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""
		password = cmd[1]
		self.password = password
		self.__authenticated = self.verifyauthentication()

		if self.__authenticated:
			command = "230 Login successful"
		else:
			command = "530 Authentication Failed"

		self.send(command)


	def verifyauthentication(self):
		"""
		Helper function to help verify authentication for a clientsocket
		:return boolean: returns a boolean {True/False} if user is authenticated or not
		"""
		if self.username in AUTHORIZED_USERS:
			if AUTHORIZED_USERS[self.username] == self.password:
				return True
			return False
		return False


	@_argumentrequired
	@_authentication
	def chdir(self, cmd):
		"""
		Change directory function to handle chdir requests
		:decorator _authentication: authentication is required for this function
		:decorator _argumentrequired: argument is required for this function
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""
		command = "250 Requested file action okay, completed"
		newcd = cmd[1]
		#if not given a full path
		if newcd[0] != "/":
			newcd = self.path + "/" + newcd

		if os.path.isdir(newcd):
			os.chdir(newcd)
			self.path = os.getcwd()

		else:
			command = "550 Requested action not taken. File unavailable"

		self.send(command)

	@_noarguments
	@_authentication
	def cdup(self, cmd):
		"""
		Change directory up function to handle cdup requests
		:decorator _authentication: authentication is required for this function
		:decorator _noarguments: no arguments are required for this request
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""
		command = "250 Requested file action okay, completed."

		newcd = self.path + "/.."
		os.chdir(newcd)
		self.path = os.getcwd()

		self.send(command)


	def quit(self, cmd):
		"""
		Quit function to handle quit requests from the client socket
		:decorator _noarguments: no arguments are required for this request
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""
		command = "221 Goodbye."
		self.send(command)
		self.connect = False
		self.socket.shutdown(socket.SHUT_WR)
		self.socket = None

	@_noarguments
	@_authentication
	def pasv(self, cmd):
		"""
		Passive function to handle pasv requests from the client socket
		:decorator _noarguments: no arguments are required for this request
		:decorator _authentication: authentication is required for this function
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""

		#get the hostname information
		hostname = socket.gethostname()
		(hostname, _, hostip) = socket.gethostbyaddr(hostname)
		host = hostip[0].replace(".", ",")

		self.passivemode = True

		#stop threads from getting the same port
		with lock:
			self.passivesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.passivesocket.bind((hostname, 0))
			self.passivesocket.listen(5)

		self.dataport = self.passivesocket.getsockname()[1]
		remainderport = self.dataport % 256

		p1 = (self.dataport - remainderport) / 256
		p2 = remainderport

		command = "227 Entering Passive Mode (%s,%s,%s)." %(host, p1, p2)
		self.send(command)

	@_noarguments
	@_authentication
	def epsv(self, cmd):
		"""
		Extended passive function to handle epsv requests from the client socket
		:decorator _noarguments: no arguments are required for this request
		:decorator _authentication: authentication is required for this function
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""

		#get hostname information
		hostname = socket.gethostname()
		(hostname, _, hostip) = socket.gethostbyaddr(hostname)

		self.passivemode = True

		#stop threads from getting the same port
		with lock:
			#bind and listen on the passive socket
			self.passivesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.passivesocket.bind((hostname, 0))
			self.passivesocket.listen(5)

		self.dataport = self.passivesocket.getsockname()[1]


		command = "229 Entering Passive Mode (|||%s)." %(self.dataport)
		self.send(command)

		
	@_argumentrequired
	@_authentication
	def port(self, cmd):
		"""
		Port function to handle port requests from the client socket, requires a valid port in request
		:decorator _argumentrequired: argument is required for this function
		:decorator _authentication: authentication is required for this function
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""
		command = "200 Port okay."
		try:
			msg = ''.join(cmd)
			pasv = msg[4:].translate(None, "().\r\n").split(",")
			p1 = int(pasv[-2])
			p2 = int(pasv[-1])

			port = (p1 * 256) + p2

			#if port out of range throw exception
			if port < 0 or port > 65535:
				raise Exception("Received port out of range " + port)

			self.dataport = port

			#Turn off passive mode
			self.passivemode = False

		except Exception as error:
			log.error(str(error), self.client)
			command = "501 Syntax error in parameters or arguments."

		self.send(command)

	@_argumentrequired
	@_authentication
	def eprt(self, cmd):
		"""
		Extended port function to handle eprt requests from the client socket
		:decorator _argumentrequired: argument is required for this function
		:decorator _authentication: authentication is required for this function
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""
		command = "200 Port okay."
		try:
			eprtdata = cmd[1]
			eprtdata = eprtdata[1:-1] #remove pipe from front and back
			af, network, port = eprtdata.split("|")

			self.dataport = int(port)

			#Turn off passive mode
			self.passivemode = False

		except Exception as error:
			log.error(str(error), self.client)
			command = "501 Syntax error in parameters or arguments."

		self.send(command)

	@_argumentrequired
	@_authentication
	def retr(self, cmd):
		"""
		Retrieve function to handle retr requests from the client socket
		requires valid file in argument request
		:decorator _argumentrequired: argument is required for this function
		:decorator _authentication: authentication is required for this function
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""
		filepath = cmd[1]
		content = ""
		try:
			with open(filepath, 'r') as openfile:
				content = openfile.read()

		except IOError as error:
			log.error("RETR " + str(error), self.client)
			command = "550 Requested action not taken. File unavailable"
			self.send(command)
			return

		command = "150 File status okay; about to open data connection."
		self.send(command)

		sockdata = []
		sockdata.append(content)

		command = self.datasocket(sockdata)
		self.send(command)


	@_argumentrequired
	@_authentication
	def stor(self, cmd):
		"""
		Stor function to handle stor requests from the client socket
		requires valid file in argument request
		:decorator _argumentrequired: argument is required for this function
		:decorator _authentication: authentication is required for this function
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""
		filepath = cmd[1]

		try:
			file = open(filepath, "w+")
			#file open now send 150
			command = "150 File status okay; about to open data connection."
			self.send(command)

			command, data = self.datasocketrecv()
			file.write(data)
			file.close()

			self.send(command)

		except IOError as error:
			log.error("stor " + str(error), self.client)
			command = "550 Requested action not taken. File unavailable"
			self.send(command)


	@_noarguments
	@_authentication
	def pwd(self, cmd):
		"""
		Print working directory function to print the current dir, calls self.path
		:decorator _noarguments: no arguments are required for this request
		:decorator _authentication: authentication is required for this function
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""
		command = "257 %s" % (self.path)
		self.send(command)

	@_noarguments
	@_authentication
	def syst(self, cmd):
		"""
		System function to print the current system the ftp server is running on
		:decorator _noarguments: no arguments are required for this request
		:decorator _authentication: authentication is required for this function
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""
		system = sys.platform
		command = "215 UNIX Type: %s" % system
		self.send(command)

	@_noarguments
	@_authentication
	def list(self, cmd):
		"""
		List function handle ls requests from client socket
		:decorator _noarguments: no arguments are required for this request
		:decorator _authentication: authentication is required for this function
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""

		#get the directory listing from the current path
		arraylist = os.listdir(self.path)
		command = "150 File status okay; about to open data connection."
		self.send(command)

		#send the listing to the datasocket
		command = self.datasocket(arraylist)
		self.send(command)


	def help(self, cmd):
		"""
		Help function that returns the availabe commands by the ftpserver
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""
		command = "214 The following commands are recognized."
		self.send(command)
		commands = ["USER PASS CWD CDUP QUIT PASV EPSV PORT EPRT RETR STOR PWD \
		SYST LIST HELP"]
		self.datasocket(commands)


	def invalid(self, cmd):
		"""
		Function that handles invalid requests made by the client socket
		:param cmd: array of the full request made from the client
		:return: returns nothing
		"""
		command = "400 %s command was not accepted and the requested action did not take place" %(cmd[0])
		self.send(command)

	def evaluation(self, command, parsedmessage):
		"""
		Evaluation function that evaluates the request made by the user and
		returns that specific function
		:param command: the command user wants to run
		:param parsedmessage: an array of the full command received by the ftp server
		:return: returns the function based on the given command
		"""
		return {
			"USER" : (self.user, parsedmessage),
			"PASS" : (self.passwd, parsedmessage),
			"CWD" : (self.chdir, parsedmessage),
			"CDUP" : (self.cdup, parsedmessage),
			"QUIT" : (self.quit, parsedmessage),
			"PASV" : (self.pasv, parsedmessage),
			"EPSV" : (self.epsv, parsedmessage),
			"PORT" : (self.port, parsedmessage),
			"EPRT" : (self.eprt, parsedmessage),
			"RETR" : (self.retr, parsedmessage),
			"STOR" : (self.stor, parsedmessage),
			"PWD" : (self.pwd, parsedmessage),
			"SYST" : (self.syst, parsedmessage),
			"LIST" : (self.list, parsedmessage),
			"HELP" : (self.help, parsedmessage),
			}.get(command, (self.invalid, parsedmessage))



class ServerSocket:
	"""
	ServerSocket establishes and opens up connections on a given port
	Attributes:
		port: the port to open the ServerSocket
		backlog: the backlog for the ServerSocket
		host: the hostname of the ServerSocket
	"""

	def __init__(self, filename="server.log", port=2121, backlog = 5):
		self.port = int(port)
		self.backlog = backlog
		self.host = socket.gethostname()
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.serversocket.bind((self.host, self.port))
		self.serversocket.listen(self.backlog)

		#log init
		msg = "Starting server on %s:%s" %(self.host, self.port)
		log.debug(msg)

	def accept(self):
		"""
		Function to accept requests on the ServerSocket
		:return: returns the clientsocket and address of the connections
		"""
		return self.serversocket.accept()

	def close(self):
		"""
		Function to close the connection of the ServerSocket
		:return: returns nothing
		"""
		self.serversocket.close()


def main():
	"""
	MAIN function, passes command line arguments into the ServerSocket, calls FTPServer to run protocol
	:return: returns nothing:
	"""

    # Runs once
    ########################################################################################
	#handle commandline arguments
	if len(sys.argv) == 3:

		filename = sys.argv[1]                                                      # filename is argv 1 ./servery.py [filename] [port]
		port = sys.argv[2]                                                          # port is argv 2

		#establish init variables {LOG, AuthorizedUsers}
		global log
		log = logger(filename, "[server]")                                          # setup up logger

		try:
			config.read(authorized_users_file)                                      # usercodes and passwords should be simulated by using separate file
			for key in config["Authorized Users"]:                                  # special parser defined at top to easily retrieve data from file
				AUTHORIZED_USERS[key] = config["Authorized Users"][key]             # storing in AUTHORIZED_USERS
		#handle invalid config file
		except (DuplicateOptionError, Error) as error:                              # Error Handling
			log.error("Error " + str(error.message), "[main]")                      # ^
			msg = "Error in %s file, Fix before proceeding" %(authorized_users_file)# ^
			log.error(msg, "[main]")                                                # ^
			exit(1)                                                                 # ^

		#Create a serversocket
		serversocket = ServerSocket(filename, port)                                 # handles info of server socket establishes and opens up connections on a given port, calls bind and listen
		ftpserver = None                                                            # just defines the variable of the soon to be ftpservre (y ?)

	else:
		log.usage("server.py <filename> <port>")
		exit(0)
    ###########################################################################################



    ###########################################################################################
	#Run the protocol for each clients
	while True:
		try:
			(clientsocket, address) = serversocket.accept()                         # Listen for connections, using socket.accept()
			msg = "Client Connected at %s:%s" %(address[0], address[1])             # Log connection
			log.debug(msg)                                                          # ^
			ftpserver = FTPServer(clientsocket, address)                            # Creating a socket server: handles the connections and status response from the clients
			ftpserver.doProtocol()                                                  # 
		#Handle CTL-C make sure threads are done running
		except KeyboardInterrupt as error:                                          # Error occured, close everything
			log.debug("Shutting down server")                                       # ^
			#if we have client running                                              # ^
			if ftpserver:                                                           # ^
				ftpserver.close()                                                   # ^
			serversocket.close()                                                    # ^
			exit()                                                                  # ^
    ############################################################################################
	
if __name__ == "__main__" :
	main()