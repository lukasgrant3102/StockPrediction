# Imports
from tkinter import *
from src.python.Graph import Graph
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


# Create app
app = QApplication([])
app.setStyle('Fusion')
window = Graph(xvalues=[0, 1, 2, 3, 4], yvalues=[100, 0, 10, 50, 33])

# Show window
window.show()
app.exec()
