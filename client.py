import socket
import time
import random
import sys

TCP_IP = "127.0.0.1"

TCP_PORT1 = 5005 # movies
TCP_PORT2 = 5008 # plays

while True:
	print("")
	request = input("How can I help you? eg. movies,10. Type quit when no more user coming:\n")
	if request == "quit":
		print("No more user.")
		break

	input_list = request.split(',')

	if input_list[0] != "movies" and input_list[0] != "plays":
		print("No such type, try again.")
		continue

	print("Message received from the user.")
	num = random.randint(1, 2)
	if num == 1:
		addr = (TCP_IP, TCP_PORT1)
		a = 'movies'
	else:
		addr = (TCP_IP, TCP_PORT2)
		a = 'plays'

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(addr)

	time.sleep(5)
	sock.sendall(request.encode('utf-8') + ','.encode('utf-8') + str(sys.argv[1]).encode('utf-8'))

	print("Message sent to the server for " + a +".")
	response = sock.recv(1024)

	if response.decode('utf-8') == 'Thank you and here are your tickets.':
		print("Here are the tickets.")
	else:
		print("Sorry, no enough ticket.")

	sock.close()
