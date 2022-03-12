import tkinter as  tk

def create_canvas(width: int, height: int) -> (tk.Canvas, ):
	master = tk.Tk()

	w = tk.Canvas(
			master,
			width=width,
			height=height
		)
	w.pack()

	w.create_line(0, y := height/2, width, y, fill="yellow")

	tk.mainloop()

create_canvas(800, 400)
