import socket
import time

TCP_IP = "127.0.0.1"
TCP_PORT = 5005

TCP_PORT_2 = 5007

SER2_IP = "127.0.0.1"
SER2_PORT = 5008

movie_ticket = 10

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.bind((TCP_IP, TCP_PORT))

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.bind((TCP_IP, TCP_PORT_2))


sock1.listen(5)
sock2.listen(5)
while True:
	stream, addr = sock1.accept()
	data = stream.recv(1024)

	tmp = (data.decode('utf-8')).split(',')
	ticket_type = tmp[0]
	ticket_num = int(tmp[1])

	if ticket_type == "movies":


		if ticket_num < movie_ticket :
			stream.sendall(("Thank you and here are your tickets.").encode('utf-8'))
			movie_ticket -= ticket_num
		else:
			stream.sendall(("No enough ticket, request denied.").encode('utf-8'))

	else:
		addr2 = (SER2_IP,SER2_PORT)
		sock2.connect(addr2)
		sock2.sendall(data)
		rep = sock2.recv(1024)
		if(rep == "Thank you ...."):
			sock1.sendall(("Thank you and here are your tickets.").encode('utf-8'))
		else:
			sock1.sendall(("No enough ticket, request denied.").encode('utf-8'))

