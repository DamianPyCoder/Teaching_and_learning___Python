import tkinter as tk

# Funciones para cambiar el color del pincel y del fondo
def set_color_blue():
    global brush_color, canvas_color
    brush_color = "blue"
    canvas_color = "white"

def set_color_green():
    global brush_color, canvas_color
    brush_color = "green"
    canvas_color = "white"

def set_color_black():
    global brush_color, canvas_color
    brush_color = "black"
    canvas_color = "white"

def set_color_red():
    global brush_color, canvas_color
    brush_color = "red"
    canvas_color = "white"

def set_color_yellow():
    global brush_color, canvas_color
    brush_color = "yellow"
    canvas_color = "white"

def set_color_purple():
    global brush_color, canvas_color
    brush_color = "purple"
    canvas_color = "white"

def set_color_orange():
    global brush_color, canvas_color
    brush_color = "orange"
    canvas_color = "white"

def set_color_pink():
    global brush_color, canvas_color
    brush_color = "pink"
    canvas_color = "white"

def set_color_light_blue():
    global brush_color, canvas_color
    brush_color = "light blue"
    canvas_color = "white"

def set_color_light_green():
    global brush_color, canvas_color
    brush_color = "light green"
    canvas_color = "white"

def set_color_white():
    global brush_color, canvas_color
    brush_color = "white"
    canvas_color = "black"

# Crear la ventana principal
root = tk.Tk()
root.title("Paint")

# Crear un frame para los botones
button_frame = tk.Frame(root)
button_frame.pack()

# Crear los botones de colores
blue_button = tk.Button(button_frame, text=" Azul ", command=set_color_blue, bg="blue", fg="lightblue", bd=0,highlightthickness=0)
blue_button.pack(side=tk.LEFT, padx=5)

green_button = tk.Button(button_frame, text=" Verde ", command=set_color_green, bg="green", fg="lightgreen", bd=0,highlightthickness=0)
green_button.pack(side=tk.LEFT, padx=5)

black_button = tk.Button(button_frame, text=" Negro ", command=set_color_black, bg="black", fg="white", bd=0,highlightthickness=0)
black_button.pack(side=tk.LEFT, padx=5)

red_button = tk.Button(button_frame, text=" Rojo ", command=set_color_red, bg="red", fg="white", bd=0,highlightthickness=0)
red_button.pack(side=tk.LEFT, padx=5)

yellow_button = tk.Button(button_frame, text=" Amarillo ", command=set_color_yellow, bg="yellow", fg="red", bd=0,highlightthickness=0)
yellow_button.pack(side=tk.LEFT, padx=5)

purple_button = tk.Button(button_frame, text=" Lila ", command=set_color_purple, bg="purple", fg="lightblue", bd=0,highlightthickness=0)
purple_button.pack(side=tk.LEFT, padx=5)

orange_button = tk.Button(button_frame, text=" Naranja ", command=set_color_orange, bg="orange", fg="yellow", bd=0,highlightthickness=0)
orange_button.pack(side=tk.LEFT, padx=5)

pink_button = tk.Button(button_frame, text=" Rosa ", command=set_color_pink, bg="pink", fg="red", bd=0,highlightthickness=0)
pink_button.pack(side=tk.LEFT, padx=5)

light_blue_button = tk.Button(button_frame, text=" Azul ", command=set_color_light_blue, bg="lightblue", fg="blue", bd=0,highlightthickness=0)
light_blue_button.pack(side=tk.LEFT, padx=5)

light_green_button = tk.Button(button_frame, text=" Verde ", command=set_color_light_green, bg="lightgreen", fg="green", bd=0,highlightthickness=0)
light_green_button.pack(side=tk.LEFT, padx=5)

white_button = tk.Button(button_frame, text=" Blanco ", command=set_color_white, bg="white", fg="grey", bd=0,highlightthickness=0)
white_button.pack(side=tk.LEFT, padx=5)

# Crear otro frame para los botones de fondo
background_blue_button = tk.Button(button_frame, text="    ", command=lambda: canvas.config(bg="blue"), bg='blue')
background_blue_button.pack(side=tk.LEFT, padx=5)

background_green_button = tk.Button(button_frame, text="    ", command=lambda: canvas.config(bg="green"), bg='green')
background_green_button.pack(side=tk.LEFT, padx=5)

background_black_button = tk.Button(button_frame, text="    ", command=lambda: canvas.config(bg="black"), bg='black')
background_black_button.pack(side=tk.LEFT, padx=5)

background_red_button = tk.Button(button_frame, text="    ", command=lambda: canvas.config(bg="red"), bg='red')
background_red_button.pack(side=tk.LEFT, padx=5)

background_yellow_button = tk.Button(button_frame, text="    ", command=lambda: canvas.config(bg="yellow"), bg='yellow')
background_yellow_button.pack(side=tk.LEFT, padx=5)

background_purple_button = tk.Button(button_frame, text="    ", command=lambda: canvas.config(bg="purple"), bg='purple')
background_purple_button.pack(side=tk.LEFT, padx=5)

background_orange_button = tk.Button(button_frame, text="    ", command=lambda: canvas.config(bg="orange"), bg='orange')
background_orange_button.pack(side=tk.LEFT, padx=5)

background_pink_button = tk.Button(button_frame, text="    ", command=lambda: canvas.config(bg="pink"), bg='pink')
background_pink_button.pack(side=tk.LEFT, padx=5)

background_light_blue_button = tk.Button(button_frame, text="    ", command=lambda: canvas.config(bg="light blue"), bg='lightblue')
background_light_blue_button.pack(side=tk.LEFT, padx=5)

background_light_green_button = tk.Button(button_frame, text="    ", command=lambda: canvas.config(bg="light green"), bg='lightgreen')
background_light_green_button.pack(side=tk.LEFT, padx=5)

background_white_button = tk.Button(button_frame, text="    ", command=lambda: canvas.config(bg="white"), bg='white')
background_white_button.pack(side=tk.LEFT, padx=5)

# Crear un canvas para dibujar
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Variables globales para el color del pincel y del fondo
brush_color = "black"
canvas_color = "white"

# Funciones para dibujar en el canvas
def paint(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    canvas.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)

def activate_paint(event):
    canvas.bind("<B1-Motion>", paint)

def deactivate_paint(event):
    canvas.unbind("<B1-Motion>")

# Enlazar el canvas con los eventos de dibujo
canvas.bind("<Button-1>", activate_paint)
canvas.bind("<ButtonRelease-1>", deactivate_paint)

# Ejecutar la ventana principal
root.mainloop()
