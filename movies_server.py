import socket
import time
import threading


class ClientThread(threading.Thread):

	def __init__(self, ip, port, conn):
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.conn = conn
		print("[*] New thread started for " + ip + ":" + str(port))

	def moviecheck(self,ticket_type,num,data):
		movie_ticket = 10
	
		if ticket_type == 'movies':
				if num <= movie_ticket :
					self.conn.sendall(('Thank you and here are your tickets.').encode('utf-8'))
					movie_ticket -= num
				else:
					self.conn.sendall(('No enough ticket, request denied.').encode('utf-8'))
		else:
			sock2.connect(addr2)
			msg = data
			print(data)
			sock2.sendall(msg)
			msg2 = sock2.recv(1024)
			sock2.close()
			self.conn.sendall(msg2)


	def run(self):
		print("Connection from: " + ip + ":" + str(port))
		data = (self.conn).recv(1024)
		print('received data: ', data)
		tmp = data.split((',').encode('utf-8'))
		ticket_type = tmp[0].decode('utf-8')
		ticket_num = int(tmp[1].decode('utf-8'))
		self.moviecheck(ticket_type,ticket_num,data)
		(self.conn).close()

TCP_IP = "127.0.0.1"
TCP_PORT = 5005

TCP_PORT_2 = 5007

SER2_IP = "127.0.0.1"
SER2_PORT = 5008


sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.bind((TCP_IP, TCP_PORT))

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.bind((TCP_IP, TCP_PORT_2))


addr2 = (SER2_IP,SER2_PORT)

sock1.listen(1)
while True:
	print("\nListening for incoming connections...")
	(stream, (ip,port)) = sock1.accept()
	newthread = ClientThread(ip,port,stream)
	newthread.run()
	# threads.append(newthread)
stream.close()

