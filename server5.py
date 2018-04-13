import socket
import time

TCP_IP = "127.0.0.1"
TCP_PORT = 5006

TCP_PORT_2 = 5008

SER1_IP = "127.0.0.1"
SER1_PORT = 5007

play_ticket = 10

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

	if ticket_type == "plays":


		if ticket_num < play_ticket :
			stream.sendall(("Thank you and here is your tickets.").encode('utf-8'))
			play_ticket -= ticket_num
			print("lol1")
		else:
			stream.sendall(("No enough tickets, request denied.").encode('utf-8'))
			print("lol2")
		stream.close()
	
	else:
                addr2 = (SER1_IP,SER1_PORT)
                sock2.connect(addr2)
                sock2.sendall(data)
                rep = sock2.recv(1024)
                if rep == "Thank you and here are your tickets." :
                        sock1.sendall(("Thank you and here are your tickets.").encode('utf-8'))
                else:
                        sock1.sendall(("No enough ticket, request denied.").encode('utf-8'))

