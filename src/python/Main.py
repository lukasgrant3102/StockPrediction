# Imports
from tkinter import *
from src.python.Graph import Graph

# Create main window
window = Tk()
window.title('Main')
window.configure(width=1000, height=800)


# Create a graph object
myGraph = Graph(window=window, xvalues=[0, 1, 2, 3, 4], yvalues=[100, 0, 10, 50, 33])
button = Button(window, text='test', bd='5', command=myGraph.myfunction)

button.pack()


window.mainloop()
