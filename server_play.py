import socket
import time
import threading
from multiprocessing import Process, Lock

class ClientThread(threading.Thread):

	def __init__(self, ip, port, conn):
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.conn = conn
		print("[*] New thread started for " + ip + ":" + str(port))

	def playcheck(self,ticket_type,num,data):
		mutex.acquire()
		global play_ticket
		if ticket_type == 'plays':
				if num <= play_ticket:
					play_ticket -= num
					mutex.release()
					time.sleep(5)
					self.conn.sendall(('Thank you and here are your tickets.').encode('utf-8'))
				else:
					mutex.release()
					time.sleep(5)
					self.conn.sendall(('No enough ticket, request denied.').encode('utf-8'))
		else:
			sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock2.connect(addr2)
			msg = data
			time.sleep(5)
			sock2.sendall(msg)
			msg2 = sock2.recv(1024)
			sock2.close()
			time.sleep(5)
			self.conn.sendall(msg2)
			mutex.release()
		self.conn.close()


	def run(self):
		print("Connection from: " + ip + ":" + str(port))
		data = (self.conn).recv(1024)
		print('received data: ', data)
		tmp = data.split((',').encode('utf-8'))
		ticket_type = tmp[0].decode('utf-8')
		ticket_num = int(tmp[1].decode('utf-8'))
		self.playcheck(ticket_type,ticket_num,data)

TCP_IP = "127.0.0.1"
TCP_PORT = 5008

TCP_PORT_2 = 5006

SER2_IP = "127.0.0.1"
SER2_PORT = 5005

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.bind((TCP_IP, TCP_PORT))

mutex = Lock()

addr2 = (SER2_IP,SER2_PORT)

play_ticket = 10

sock1.listen(1)
while True:
	print("\nListening for incoming connections...")
	(stream, (ip,port)) = sock1.accept()
	newthread = ClientThread(ip,port,stream)
	newthread.run()
	# threads.append(newthread)
stream.close()
