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
		self.dataport = 20 #default 20                      #That side port to send heaps of data
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

    #################################################################################################
    #THE REAL MAIN, notice the protocol starts on a thread, the main thread doesn't go into protocol
    #################################################################################################
	def _thread(function):
		"""
		Decorator function to handle if an argument is required for that function
		:param function: the function that requires an argument eg {CD <argument>}
		:return: returns the function or returns nothing
		"""
		def threadwrapper(self, *args):
			thread = threading.Thread(target=function, args=(self, ))                   # Creates a new thread
			thread.start()                                                              # Runs the function on a new thread, main thread ignores this

		return threadwrapper


	@_thread
	def doProtocol(self):
		"""
		Function that will run the FTP protocol threaded and continuously
		:return: returns nothing
		"""
		self.welcome()
		while self.connect:                                                             # LOOP WHILE CONNECTED
			try:
				message = self.receive()                                                # recieve input
				if message:                                                             # if recieved input
					log.received(message, self.client)                                  # > log input
					parsedmessage = message.split()                                     # > plit input into command, and message (ex: PORT 2000)
					(function, cmd) = self.evaluation(parsedmessage[0], parsedmessage)  # > evaluate the command, return corresponding function and parsedmessage
					function(cmd)                                                       # > run returned function, passing parsedmessage
				elif not connected:                                                     # else if (connection broke)
					break                                                               # > leave while loop
			except socket.error as error:                                               # Error Handling
				msg = "Client Disconneted %s" %self.client                              # ^
				log.debug(msg)                                                          # ^
				break                                                                   # ^

    ###################################################################################################

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



    ##########################################################################################################
	def datasocket(self, command=None):
		"""
		Function that handles sending data on the datasocket for active and passive mode
		:param command: the command from the server to send to the client
		:return: returns the response of the status of the data transfer
		"""
		response = "425 Can't open dataconnection"
		try:
			dsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                         # Create a new socket
			if self.passivemode:                                                                # Check to see if we
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
#################################################################################################################


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
			ftpserver.doProtocol()                                                  # puts user into new thread, and main thread returns waiting for new connection
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