import tkinter as tk

def create_rectangle(canvas, x1, y1, x2, y2, **kwargs):
    return canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

def on_left_click(event):
    global selected_rectangle, last_x, last_y
    item = canvas.find_closest(event.x, event.y)
    if item and canvas.type(item) == "rectangle":
        selected_rectangle = item
        last_x = event.x
        last_y = event.y

def on_left_drag(event):
    global last_x, last_y
    if selected_rectangle:
        dx = event.x - last_x
        dy = event.y - last_y
        canvas.move(selected_rectangle, dx, dy)
        last_x = event.x
        last_y = event.y

def on_left_release(event):
    global selected_rectangle
    selected_rectangle = None

root = tk.Tk()
root.title("Déplacement de rectangles")

canvas = tk.Canvas(root, bg="white", width=400, height=400)
canvas.pack()

rectangle1 = create_rectangle(canvas, 50, 50, 150, 100, fill="blue")
rectangle2 = create_rectangle(canvas, 200, 200, 300, 250, fill="red")

selected_rectangle = None
last_x = 0
last_y = 0

canvas.bind("<Button-1>", on_left_click)
canvas.bind("<B1-Motion>", on_left_drag)
canvas.bind("<ButtonRelease-1>", on_left_release)

root.mainloop()