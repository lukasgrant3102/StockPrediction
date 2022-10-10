# Imports
from tkinter import *
from src.python.Graph import Graph
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


# Create app
app = QApplication([])
app.setStyle('Fusion')
window = Graph(xvalues=[0, 1, 2, 3, 4], yvalues=[100, 0, 10, 50, 33])

"""
# Set window layout
layout = QVBoxLayout()
window.setLayout(layout)

# Create button widgets
topButton = QPushButton('Top')


# Define button functions
def print_test():
    print("this button works!")


# Connect functions to buttons
topButton.clicked.connect(print_test)

# Add widgets to window
layout.addWidget(topButton)
"""


# Show window
window.show()
app.exec()

"""
# Create main window
window = Tk()
window.title('Main')
window.configure(width=1000, height=800)




# Create a graph object
myGraph = Graph(window=window, xvalues=[0, 1, 2, 3, 4], yvalues=[100, 0, 10, 50, 33])
button = Button(window, text='test', bd='5', command=myGraph.myfunction)

button.pack()


window.mainloop()
"""
