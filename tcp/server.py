from socket import socket

PORT = 2000

s = socket()

s.bind(('', PORT))
s.listen(5)

while True:
	c, addr = s.accept()

	print("Got connection from", addr)

	dados = c.recv(1024)
	print("Received:", dados.decode())

	c.send(b'Thanks for connecting')
