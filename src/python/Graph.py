# Imports
from tkinter import *

# Graph properties
x_title = "X-Axis"
y_title = "Y-Axis"

x_max = 100
y_max = 100

# Window Properties
width = 1000
height = 800
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
# y line
canvas.create_line(100, 50, 100, height-100)
# x line
canvas.create_line(100, height-100, width-100, height-100)

y_axis_line_length = (height - 100) - 50
x_axis_line_length = (width - 100) - 100

# Determined from above (not automatically)
# distance from left side of window to y-axis
y_axis_offset = 100
# distance from top of window to x-axis
x_axis_offset = height-100

# Data set
prices = [10, 20, 30, 20, 10, 5, 40, 10]
dates = [1, 2, 3, 4, 5, 6, 7, 8]

# Determining min, max, and range of data set
price_min = min(prices)
price_max = max(prices)
price_range = price_max - price_min

# Storing coordinates for line values
x_coord_list = []
y_coord_list = []

# Creating list of evenly distributed values between min and max prices
step = (price_max - price_min) / float(len(dates)-1)
list_prices = [int(round(price_min+x*step)) for x in range(len(dates))]

# Create lines and labels for x-axis
for i in range(len(prices)):
    lineXPos = ((i+1) * (x_axis_line_length / len(prices))) + y_axis_offset
    x_coord_list.append(lineXPos)
    canvas.create_line(lineXPos, x_axis_offset - 5, lineXPos, x_axis_offset + 5)
    canvas.create_text(lineXPos, x_axis_offset + 12, text=str(dates[i]), font='arial 7')

# Create lines and labels for y-axis
for i in range(len(dates)):
    lineYPos = (i * (y_axis_line_length / len(dates))) + 50
    canvas.create_line(y_axis_offset - 5, lineYPos, y_axis_offset + 5, lineYPos)
    canvas.create_text(y_axis_offset - 12, lineYPos, text=str(list_prices[(len(dates) - i) - 1]), font='arial 7')


# Creates a point on the given canvas at the given coordinates
def create_point(param_canvas, x, y):
    param_canvas.create_oval(x-2, y-2, x+2, y+2, fill='black')


# Loops through and creates points at price values
for i in range(len(prices)):
    y_coord_list.append((prices[i] / price_max) * y_axis_line_length)
    create_point(canvas, x_coord_list[i], y_coord_list[i])

for i in range(len(x_coord_list) - 1):
    canvas.create_line(x_coord_list[i], y_coord_list[i], x_coord_list[i+1], y_coord_list[i+1])


canvas.pack()

window.mainloop()




