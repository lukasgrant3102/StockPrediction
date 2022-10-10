# Graph class created by Lukas Grant
# Imports
from tkinter import *
from qtpy import QtGui, QtCore


class Graph:
    # Graph properties
    x_title = "X-Axis"
    y_title = "Y-Axis"

    # Graph data
    x_values = []
    y_values = []

    # Properties
    # canvas = None
    # window = None
    # width = 600
    # height = 400
    background_color = 'lightgray'
    font = 'arial 10 bold'

    # Creates a point on the given canvas at the given coordinates
    @staticmethod
    def create_point(param_canvas, x, y):
        param_canvas.create_oval(x-2, y-2, x+2, y+2, fill='black')

    def __init__(self, window, xvalues, yvalues):
        self.width = 600
        self.height = 400

        self.canvas = Canvas(window, width=self.width, height=self.height, bg=self.background_color)
        print('canvas created with height = ' + str(self.height))
        self.x_values = xvalues
        self.y_values = yvalues

        # x-axis text
        self.canvas.create_text(self.width / 2, self.height - 15, text=self.x_title, font=self.font)

        # Axis lines
        # y line
        self.canvas.create_line(100, 50, 100, self.height - 100)
        # x line
        self.canvas.create_line(100, self.height - 100, self.width - 100, self.height - 100)

        y_axis_line_length = (self.height - 100) - 50
        x_axis_line_length = (self.width - 100) - 100

        # Determined from above (not automatically)
        # distance from left side of window to y-axis
        y_axis_offset = 100
        # distance from top of window to x-axis
        x_axis_offset = self.height - 100

        # Determining min, max, and range of data set
        y_min = min(self.y_values)
        y_max = max(self.y_values)
        price_range = y_max - y_min

        # Storing coordinates for line values
        x_coord_list = []
        y_coord_list = []

        # Creating list of evenly distributed values between min and max prices
        step = (y_max - y_min) / float(len(self.y_values) - 1)
        list_prices = [int(round(y_min + (i * step))) for i in range(len(self.x_values))]

        # Create lines and labels for x-axis
        for i in range(len(self.x_values)):
            multiplier = i * len(self.x_values) / (len(self.x_values) - 1)
            linexpos = (multiplier * (x_axis_line_length / len(self.y_values))) + y_axis_offset
            x_coord_list.append(linexpos)
            self.canvas.create_line(linexpos, x_axis_offset - 5, linexpos, x_axis_offset + 5)
            self.canvas.create_text(linexpos, x_axis_offset + 12, text=str(self.x_values[i]), font='arial 7')

        # Create lines and labels for y-axis
        for i in range(len(self.y_values)):
            multiplier = i * len(self.y_values) / (len(self.y_values) - 1)
            lineypos = (multiplier * (y_axis_line_length / len(self.x_values))) + 50
            self.canvas.create_line(y_axis_offset - 5, lineypos, y_axis_offset + 5, lineypos)
            self.canvas.create_text(y_axis_offset - 12, lineypos, text=str(list_prices[len(self.y_values) - (i + 1)]),
                                    font='arial 7')

        # Loops through and creates points at price values
        for i in range(len(self.y_values)):
            y_coord_list.append(((1 - (self.y_values[i] / y_max)) * y_axis_line_length) + 50)
            self.create_point(self.canvas, x_coord_list[i], y_coord_list[i])

        for i in range(len(x_coord_list) - 1):
            self.canvas.create_line(x_coord_list[i], y_coord_list[i], x_coord_list[i + 1], y_coord_list[i + 1])

        self.canvas.pack()

    # Returns the list of x_values
    def get_x_values(self):
        return self.x_values

    # Returns the list of y_values
    def get_y_values(self):
        return self.y_values

    def get_height(self):
        return self.height

    def myfunction(self):
        self.canvas.create_line(0, 100, 150, 200)
