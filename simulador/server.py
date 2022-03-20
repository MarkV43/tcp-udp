from simulator import get_terminated, terminate, set_F, get_th, get_xv
from time import sleep
import socket


ip = socket.gethostbyname('localhost')
port = 3000
bufferSize = 1024

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind((ip, port))

def run_server():
	global udp_server
	udp_server.settimeout(1)
	while not get_terminated():
		try:
			value = float(udp_server.recvfrom(bufferSize)[0].decode())
			set_F(value)
		except socket.timeout:
			pass
		x, th = get_xv(), get_th()
		udp_server.sendto(f"{x};{th}".encode(), (ip, port+1))
	udp_server.sendto(b"STOP", (ip, port+1))

