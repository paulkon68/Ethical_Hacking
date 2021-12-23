# this library manages multiple TCP connections.
import socketserver

class BotHandler(socketserver.BaseRequestHandler):

	def handle(self):
		# self.data = self.request.recv(1024).strip()
		# print('Bot with IP {} sent:'.format(self.client_address[0]))
		# print(self.data)
		# self.request.sendall(self.data.upper())
		with open('commands.sh') as file:
			for command in file:
			    self.request.sendall(command.encode())


if __name__ == '__main__':
	
	HOST, PORT = "", 8000
	tcpServer = socketserver.TCPServer((HOST, PORT), BotHandler)
	try:
		tcpServer.serve_forever()
	except:
		print('The was an error')

