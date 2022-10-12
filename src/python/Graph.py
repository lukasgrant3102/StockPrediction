# Graph class created by Lukas Grant
# Imports
from tkinter import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Graph(QWidget):
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
    def create_point(painter, x, y):
        painter.drawEllipse(x - 2, y - 2, 4, 4)

    def __init__(self, xvalues, yvalues, parent):
        super().__init__(parent)
        self.width = 600
        self.height = 400

        self.x_values = xvalues
        self.y_values = yvalues

    def paintEvent(self, event):
        # Create painter object
        painter = QPainter(self)

        # Create background
        painter.fillRect(0, 0, 800, 600, Qt.white)

        painter.setPen(Qt.black)

        # x-axis text
        painter.drawText(self.width / 2, self.height - 15, self.x_title)

        # Axis lines
        # y line
        painter.drawLine(100, 50, 100, self.height - 100)
        # x line
        painter.drawLine(100, self.height - 100, self.width - 100, self.height - 100)

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
            painter.drawLine(linexpos, x_axis_offset - 5, linexpos, x_axis_offset + 5)
            painter.drawText(linexpos - 3, x_axis_offset + 16, str(self.x_values[i]))

        # Create lines and labels for y-axis
        for i in range(len(self.y_values)):
            multiplier = i * len(self.y_values) / (len(self.y_values) - 1)
            lineypos = (multiplier * (y_axis_line_length / len(self.x_values))) + 50
            painter.drawLine(y_axis_offset - 5, lineypos, y_axis_offset + 5, lineypos)
            painter.drawText(y_axis_offset - 25, lineypos + 4, str(list_prices[len(self.y_values) - (i + 1)]))

        # Loops through and creates points at price values
        for i in range(len(self.y_values)):
            y_coord_list.append(((1 - (self.y_values[i] / y_max)) * y_axis_line_length) + 50)
            self.create_point(painter, x_coord_list[i], y_coord_list[i])

        for i in range(len(x_coord_list) - 1):
            painter.drawLine(x_coord_list[i], y_coord_list[i], x_coord_list[i + 1], y_coord_list[i + 1])



    # Returns the list of x_values
    def get_x_values(self):
        return self.x_values

    # Returns the list of y_values
    def get_y_values(self):
        return self.y_values

    # Set the object's x value list
    def set_x_values(self, xvalues):
        self.x_values = xvalues

    # Set the object's y value list
    def set_y_values(self, yvalues):
        self.y_values = yvalues

    # Returns the width of the graph
    def get_width(self):
        return self.width

    # Returns the height of the graph
    def get_height(self):
        return self.height

