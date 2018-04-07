from multiprocessing import Process, Lock
import socket
import time
import random

mutex = Lock()

def kiosk(kid):
	with mutex:
		TCP_IP1 = "127.0.0.1" # plays
		TCP_IP2 = "127.0.0.2" # movies

		# TCP_PORT = random.randint(5000, 10000)
		TCP_PORT = 5005

		# while True:
		# 	print("A new user comes!")

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		while True:
			request = input("How can I help you? eg. movies,10. Type quit to when no more user coming:\n")
			if request == "quit":
				print("No more user.")
				break

			print("Message received from the user.")
			num = random.randint(1, 2)
			if num == 1:
				addr = (TCP_IP1, TCP_PORT)
			else:
				addr = (TCP_IP2, TCP_PORT)

			sock.connect(addr)

			sock.sendall(request.encode('utf-8') + ",".encode('utf-8') + kid.encode('utf-8'))
			print("Message sent to the server.")
			response = sock.recv(1024)

			if response == "success":
				print("Here are the tickets.")
			else:
				print("Sorry, no enough ticket.")

			sock.close()
