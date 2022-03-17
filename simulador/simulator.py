from math import sin, cos, pi
import string
from time import sleep, time as f_time
from p5 import *
import threading
import sys
import socket
from socketserver import UDPServer


ip = "127.0.0.1"
port = 20001
bufferSize = 1024
serverAddressPort = (ip, port)

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.bind(serverAddressPort)

def send_recv_udp(msg: str):
	global UDPClientSocket
	UDPClientSocket.sendto(msg.encode(), serverAddressPort)
	return UDPClientSocket.recvfrom(bufferSize)

"""
Let's create a system simulation
The EDOs will be defined as follows

"""
# Define the constants
m = 4000 # Kg
M = 496 # Kg
l = 3 # m
path = 21 # m
xv = 0 # m
xv_d = 0 # m/s
xv_dd = 0 # m/s^2
th = 0 # rad
th_d = 0 # rad/s
th_dd = 0 # rad/s^2
F = 0 # N
g = 9.81 # m/s^2
b = 100
d = 100

delta_time = 0.01 # s or 100 Hz

terminated = False

def ode_generator():
	global xv, xv_d, xv_dd, th, th_d, th_dd, F, g, b, d
	# Initial Conditions
	xv = 0
	xv_d = 0
	xv_dd = 0
	th = pi/3
	th_d = 0
	th_dd = 0
	F = 1
	start = f_time()

	while True:
		# First calculate x_dd and theta_dd
		try:
			xv_dd = (1 / (M + m * sin(th) ** 2)) * (m * th_d * th_d * l * sin(th) + m * cos(th) * (g * sin(th) + b * th_d / (m * l)) + F - d * xv_d)
			th_dd = -1/l * cos(th)/ (M + m * sin(th) ** 2) * (m * th_d * th_d * l * sin(th) + m * cos(th) * (g * sin(th) + b * th_d / (m * l)) + F - d * xv_d) - g * sin(th) / l - b * th_d / (m * l * l)
		except ValueError:
			print('Error:\nxv_dd: {}\nxv_d: {}\nxv: {}\ntheta_dd: {}\ntheta_d: {}\ntheta: {}'.format(xv_dd, xv_d, xv, th_dd, th_d, th))
			break

		# Calculate numeric integrals
		xv_d += xv_dd * delta_time
		th_d += th_dd * delta_time
		xv += xv_d * delta_time
		th += th_d * delta_time

		yield xv, th


def run():
	# Let's create a generator
	ode_gen = ode_generator()

	udp_frequency = 10 # Hz
	udp_time = 1/udp_frequency # s

	total = 0
	last = f_time()

	for xv, theta in ode_gen:
		if total >= udp_time:
			send_recv_udp(f"{xv};{theta}")
			total -= udp_time
		total += delta_time
		sleep(delta_time)
		# Show framerate
		print(1 / (-last + (last := f_time())))
		if terminated:
			break

def terminate():
	global terminated
	terminated = True

def get_xv():
	return xv

def get_th():
	return th

def get_F():
	return F
