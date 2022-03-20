import tkinter as tk
from server import run_server
from simulator import run, get_xv, get_th, get_F, l, path, terminate
from canvas import create_canvas
from math import sin, cos
import threading


def update():
	global canvas, l
	draw(parent, canvas, get_xv(), get_th(), l)

def transform(x, y):
	global scale, x_off, y_off
	return (x * scale + x_off, y * scale + y_off)

def line(canvas, x1, y1, x2, y2, **kwargs):
	p1 = transform(x1, y1)
	p2 = transform(x2, y2)
	canvas.create_line(*p1, *p2, **kwargs)

def circle(canvas, c1, c2, r, **kwargs):
	rn = r * scale
	x, y = transform(c1, c2)
	canvas.create_oval(x-rn, y-rn, x+rn, y+rn, **kwargs)

def draw(parent, cvs, xv, th, l):
	cvs.delete("all")
	line(cvs, -path/2, 0, path/2, 0, fill='grey', width=1)
	line(cvs, xv, 0, xv + get_F()/600, 0, fill='blue', width=1, arrow=tk.LAST)
	tip = xv + sin(th) * l, cos(th) * l
	line(cvs, xv, 0, *tip, fill='#f00', width=2)
	circle(cvs, *tip, 0.3, fill='#f00')
	cvs.update()
	parent.after(10, update)

if __name__ == '__main__':
	x = threading.Thread(target=run)
	y = threading.Thread(target=run_server)
	x.start()
	y.start()

	width, height = 800, 300
	parent, canvas, start = create_canvas(width, height)

	# Center at (width/2, l * scale)
	# Will leave `l` meters on each side of path, that is `path` meters long

	scale = width / (path + 2 * l)
	x_off = width / 2
	y_off = l * scale

	parent.after(0, update)
	start()
	terminate()
	x.join()
	y.join()

