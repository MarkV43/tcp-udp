from socket import *

PORT = 2000

s = socket(AF_INET, SOCK_STREAM)

address = gethostbyname('localhost')
s.connect((address, PORT))

s.send(b"Hello!")

msg = s.recv(1024)
print(msg.decode())

s.send(b"Bye!")
s.close()
