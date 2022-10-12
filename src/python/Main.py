# Imports
from tkinter import *
from src.python.Graph import Graph
from PyQt5.QtWidgets import *

# Create app
app = QApplication([])
app.setStyle('Fusion')

# Create layouts
mainLayout = QHBoxLayout()
graphLayout = QVBoxLayout()
otherLayout = QVBoxLayout()

# Create window and sections
window = QWidget()
window.setLayout(mainLayout)

graphSection = QWidget()
otherSection = QWidget()

# Set layouts of sections
graphSection.setLayout(graphLayout)
otherSection.setLayout(otherLayout)

# Set geometry of sections
window.setGeometry(300, 300, 800, 600)
graphSection.setGeometry(0, 0, 600, 600)
otherSection.setGeometry(400, 0, 100, 100)

# Create graph
graph = Graph(xvalues=[0, 1, 2, 3, 4], yvalues=[100, 0, 10, 50, 33])

# Create buttons
button = QPushButton()
button.setText('test')

# Add widgets to the layouts
mainLayout.addWidget(graphSection)
mainLayout.addWidget(otherSection)

graphLayout.addWidget(graph)
otherLayout.addWidget(button)







# Define button functions
    # new_graph = Graph(xvalues=[0, 1, 2, 3, 4], yvalues=[0, 30, 10, 50, 100])
    # layout.addWidget(new_graph)

# Connect button clicks to functions



# Show window
window.show()




app.exec()

