import tkinter as tk
from tkinter import ttk


class Root(tk.Tk):
    size = ["Small", "Medium", "Large"]

    def __init__(self, menu):
        super(Root, self).__init__()
        self.menu = menu
        self.frame = tk.Frame(self, height=500, width=500, bg="white")
        self.init_setup()
        self.start_button = tk.Button(self.frame, text="Start Game", command=self.minesweeper_mode)
        self.end_button = tk.Button(self.frame, text="End Game", command=lambda: self.menu.end_game("quit"))
        self.size_button = ttk.Combobox(self.frame, values=self.size)
        self.main_menu_mode()

    def init_setup(self):
        self.title("Minesweeper")
        self.minsize(500, 500)
        self.maxsize(500, 500)
        self.frame.pack()

    def main_menu_mode(self):
        self.change_size(500)
        self.end_button.place_forget()
        self.start_button.place(relx=0.5, rely=0.49)
        self.size_button.place(relx=0.1, rely=0.5)
        self.size_button.set("Pick a size")

    def minesweeper_mode(self):
        if self.size_button.get() == "Small":
            self.change_size(400)
        elif self.size_button.get() == "Medium":
            self.change_size(560)
        elif self.size_button.get() == "Large":
            self.change_size(700)
        else:
            return
        self.start_button.place_forget()
        self.size_button.place_forget()
        self.menu.start_game(self.size_button.get())

    def change_size(self, num):
        self.minsize(num, num)
        self.maxsize(num, num)
        self.frame.config(height=num, width=num)
        self.end_button.place(relx=0.45, y=num-40)
