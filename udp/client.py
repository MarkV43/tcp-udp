from socket import *

PORT = 5000

udp = socket(AF_INET, SOCK_DGRAM)

while True:
	msg = input("\nDigite um texto para enviar:\n")

	udp.sendto(msg.encode(), ('localhost', PORT))

	if len(msg) == 0:
		break

udp.close()
