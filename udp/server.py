from socket import *

PORT = 5000

udp = socket(AF_INET, SOCK_DGRAM)
udp.bind(('', PORT))

while True:
	msg, c = udp.recvfrom(3000)

	if len(msg) == 0:
		break

	print(c, msg.decode())

udp.close()
