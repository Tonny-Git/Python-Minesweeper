from tkinter import *


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Minesweeper")
        self.minsize(500, 500)
        self.maxsize(1000, 1000)
        frame = Frame(self, height=500, width=500, bg="white").pack()
