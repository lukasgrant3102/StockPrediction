import tkinter
from tkinter import *

window = Tk()
window.title('Stock Predictor')

window.configure(width='800', height='600')
window.configure(bg='lightgray')

canvas = Canvas(window, width=500, height=400, bg='red')
canvas.pack()


def my_command():
    canvas.create_line(0, 0, 100, 100)


myButton = tkinter.Button(canvas, text='button', command=my_command)
myButton.pack()

window.mainloop()
