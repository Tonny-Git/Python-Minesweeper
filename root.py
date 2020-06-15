import tkinter as tk


class Root(tk.Tk):

    def __init__(self, menu):
        super(Root, self).__init__()
        self.menu = menu
        self.init_setup()
        self.frame = tk.Frame(self, height=700, width=700, bg="white").pack()
        self.start_button = tk.Button(self.frame, text="Start Game", command=self.minesweeper_mode)
        self.main_menu_mode()

    def init_setup(self):
        self.title("Minesweeper")
        self.minsize(700, 700)
        self.maxsize(700, 700)

    def main_menu_mode(self):
        self.start_button.place(relx=0.45, rely=0.5)

    def minesweeper_mode(self):
        self.menu.start_game()
