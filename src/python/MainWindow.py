# Imports
from src.python.Graph import Graph
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import *
from PyQt5.QtGui import *


def test():
    print('button works')


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # Window values
        self.setMinimumSize(QSize(800, 600))
        self.setWindowTitle("Stock Predictor")
        self.setGeometry(300, 300, 800, 600)

        # Add widgets
        myButton = QPushButton('button!', self)
        myButton.resize(100, 30)
        myButton.move(50, 50)
        myButton.clicked.connect(test)

        self.myGraph = Graph(xvalues=[0, 1, 2, 3, 4], yvalues=[100, 0, 10, 50, 33], parent=self)
        self.myGraph.resize(600, 400)
        self.myGraph.move(100, 100)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
