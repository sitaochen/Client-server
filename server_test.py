# Echo server program
import socket

HOST = "127.0.0.1"                 # Symbolic name meaning all available interfaces
PORT = 5007              # Arbitrary non-privileged port

movie_ticket = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while 1:
	conn, addr = s.accept()
	print('Connected by', addr)
	data = conn.recv(1024)
	if not data: break
	tmp = data.split((',').encode('utf-8'))
	ticket_type = tmp[0].decode('utf-8')
	ticket_num = int(tmp[1].decode('utf-8'))
	if str(ticket_type) == "movies" :
		if ticket_num <= movie_ticket :
			conn.sendall(('Thank you and here are your tickets.').encode('utf-8'))
			movie_ticket -= ticket_num
		else:
			conn.sendall(('No enough ticket, request denied.').encode('utf-8'))
	else:
		conn.sendall(('movies can not be identified.').encode('utf-8'))
conn.close()