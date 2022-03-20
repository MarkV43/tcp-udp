import socket
import threading

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = socket.gethostbyname('localhost')

tcp.connect((addr, 2001))

# tcp.send(b"PANEL")

def main():
	global tcp

	terminate = False
	while not terminate:
		text = input("\nWhat's the new setpoint?\n")
		if text.upper() == 'STOP':
			terminate = True
			continue

		try:
			setpoint = float(text)
		except ValueError:
			continue

		tcp.send(f"{setpoint}".encode())

	tcp.close()





if __name__ == '__main__':
	main()
