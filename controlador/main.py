from time import sleep
from controlador import Controlador
import socket
from sys import stderr
import threading

terminate = False
cont = Controlador()

def run_udp():
	global udp_server

	ip = socket.gethostbyname('localhost')
	port = 3001
	bufferSize = 1024

	udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	udp_server.bind((ip, port))

	def send_recv_udp(msg: str):
		global udp_server
		udp_server.sendto(msg.encode(), (ip, port-1))
		udp_server.settimeout(1)
		m = udp_server.recvfrom(bufferSize)[0].decode()
		if m == 'STOP':
			global terminate
			terminate = True
			return (0, 0)
		else:
			return [float(k) for k in m.split(';')]

	global terminate, cont

	udp_frequency = 10 # Hz
	udp_period = 1 / udp_frequency # s
	theta = 0
	xv = 0

	while not terminate:
		try:
			xv, theta = send_recv_udp(str(cont.next(theta, xv)))
			# print(f"xv = {xv}\ttheta = {theta}")
			sleep(udp_period)
		except Exception as e:
			print(f"Error: {e}")

def run_tcp():
	global terminate

	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	tcp.bind(('', 2001))
	tcp.listen(1)

	while not terminate:
		c, addr = tcp.accept()

		try:
			print(f"Connection frpm {addr}")

			while True:
				data = c.recv(1024)
				print(f"Received: {data.decode()}")

				if data != 'STOP':
					cont.set_setpoint(float(data))
				else:
					terminate = True
					break

		finally:
			c.close()


if __name__ == '__main__':
	x = threading.Thread(target=run_tcp)
	y = threading.Thread(target=run_udp)
	x.start()
	y.start()
	x.join()
	y.join()
