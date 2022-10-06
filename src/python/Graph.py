# Imports
from tkinter import *

# Graph properties
x_title = "X-Axis"
y_title = "Y-Axis"

x_max = 100
y_max = 100

x_increments = 8
y_increments = 8

# Window Properties
width = 800
height = 600
background_color = 'lightgray'
font = 'arial 10 bold'

# Create window
window = Tk()
window.title("Graph")
window.configure(width=width, height=height)
window.configure(bg='white')

canvas = Canvas(window, width=width, height=height, bg=background_color)
# x-axis text
canvas.create_text(width/2, height - 15, text=x_title, font=font)

# Axis lines
canvas.create_line(100, 50, 100, height-100)
canvas.create_line(100, height-100, width-100, height-100)


prices = [10, 20, 30, 20, 10, 5, 40, 10]
dates = []

canvas.pack()

window.mainloop()

