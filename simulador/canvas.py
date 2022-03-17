import tkinter as  tk

def create_canvas(width: int, height: int):
	master = tk.Tk()

	w = tk.Canvas(
			master,
			width=width,
			height=height,
			bg='black'
		)
	w.pack()

	return master, w, lambda: tk.mainloop()
