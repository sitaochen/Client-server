from multiprocessing import Process, Lock
import socket
import time

TCP_IP = "192.168.253.253"
TCP_PORT = 5005;

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))

sock.listen(1)
while True:
	stream, addr = sock.accept()
	data = stream.recv(1024)

	print(data.decode('utf-8'))
	stream.close()
