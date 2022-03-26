import socket


host = socket.gethostbyname(socket.gethostname())
print("host ip:", host)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind( (host,2121) )
serversocket.listen(5)

(clientsocket, address) = serversocket.accept()
with clientsocket:
    clientsocket.sendall(b"Welcome\r\n")
    print("Got a user")

    
    def read():
        response = ""
        while True:
            clientsocket.settimeout(1)
            mess = clientsocket.recv(1024)
            response += mess.decode('utf-8')
            print("a message recieved")
            if not mess:
                print("break")
                break

        return response

    
    def write(mess):
        try:
            clientsocket.sendall( bytes(mess + "\r\n") )
        except socket.error as e:
            print("error:", str(e))

    print("Now beginning reading")
    mess = read()
    print("Now beginning writing")
    write(mess)


    print("Ok Closing Socket Now!")

    clientsocket.shutdown(socket.SHUT_WR)
    serversocket.close()