import tkinter as tk

from minesweeper_board import MinesweeperBoard
from game_setting import Setting
from timer import Timer

class Menu:


    def __init__(self, root):
        self.root = root
        self.settings = Setting()
        self.button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.end_button = tk.Button(self.root, text="End Game", command=lambda: self.end_game("quit"))
        # self.time_label = tk.Label(self.root, text='')
        # self.time = 0
        self.timer = ""
        self.start_menu()
        self.board = []
        self.buttons = []
        # This "fake" image fixes button size to pixels instead of text
        self.image = tk.PhotoImage(width=0, height=1)

    def start_menu(self):
        self.button.place(relx=0.45, rely=0.5)

    # removes start button and adds minesweeper buttons
    def start_game(self):
        self.button.place_forget()
        self.end_button.place(relx=0.45, rely=0.9)
        self.board = MinesweeperBoard(self.settings.board_size["medium"], self.settings.board_size["medium"])  # Fix sizing issues
        self.timer = Timer(self.root)
        # x = 0
        # y = 0
        for i in range(self.board.rows):
            temp_buttons = []
            for j in range(self.board.columns):
                button = tk.Button(self.root, image=self.image, bg=self.settings.colors["button"],
                                   width=22, height=22, text=" ", compound="c")
                button.config(command=lambda btn=button, board_btn=self.board.buttons[i][j], row=i, col=j: self.reveal_buttons(row, col))
                button.bind("<Button-2>", self.place_flag)
                button.bind("<Button-3>", self.place_flag)
                button.place(x=self.board.buttons[i][j].x, y=self.board.buttons[i][j].y)
                temp_buttons.append(button)
            self.buttons.append(temp_buttons)

    # Reveals the pressed button and if it is empty triggers all around to reveal itself.
    def reveal_buttons(self, row, col):
        self.buttons[row][col].config(text=self.board.buttons[row][col].value, state=tk.DISABLED, relief=tk.RIDGE, disabledforeground="#000000")

        if self.board.buttons[row][col].value == " ":
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if self.board.rows > row+i >= 0 and self.board.columns > col+j >= 0 and self.board.buttons[row+i][col+j].value != "X" and self.buttons[row+i][col+j]["state"] != tk.DISABLED:
                        self.buttons[row+i][col+j].config(text=self.board.buttons[row+i][col+j].value, state=tk.DISABLED, relief=tk.RIDGE, disabledforeground="#000000")
                        self.reveal_buttons((row+i), (col+j))
        self.game_status_check(row, col)

    # Checks the state of game.
    def game_status_check(self, row, col):
        if self.board.buttons[row][col].value == "X":
            self.buttons[row][col].config(bg=self.settings.colors["mine"])
            self.end_game("lost")
        else:
            bombs_remaining = len(self.buttons) * len(self.buttons[0]) * 0.1
            buttons_remaining = 0
            for row in self.buttons:
                for button in row:
                    if button["state"] != tk.DISABLED:
                        buttons_remaining += 1

            if bombs_remaining == buttons_remaining:
                self.end_game("won")

    # Toggles "flag" color on right/middle click
    def place_flag(self, event):
        if event.widget["bg"] == self.settings.colors["button"] and event.widget["state"] != tk.DISABLED:
            event.widget.configure(bg=self.settings.colors["flag"])
        else:
            event.widget.configure(bg=self.settings.colors["button"])

    # Work on this!!!
    def end_game(self, end_condition):
        self.timer.isActive = False

        if end_condition == "won":
            for row in self.buttons:
                for button in row:
                    if button["state"] != tk.DISABLED:
                        button.config(bg=self.settings.colors["victory"])
            self.disable_all_buttons()
        elif end_condition == "lost":
            self.disable_all_buttons()
            print("lost")  # Fix this
        elif end_condition == "quit":
            for row in range(self.board.rows):
                for col in range(self.board.columns):
                    self.buttons[row][col].destroy()
            self.end_button.place_forget()
            self.buttons = []
            self.timer.time_label.destroy()
            self.start_menu()

    # Disables all minesweeper buttons
    def disable_all_buttons(self):
        for row in range(self.board.rows):
            for col in range(self.board.columns):
                self.buttons[row][col].config(state=tk.DISABLED, disabledforeground="#000000")