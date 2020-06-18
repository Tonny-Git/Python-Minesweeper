import tkinter as tk

from Tkinter.root import Root
from Components.minesweeper_board import MinesweeperBoard
from Tkinter.game_setting import Setting
from Components.timer import Timer
from sqlite import Database


class Menu:

    def __init__(self):
        self.score = Database()
        self.root = Root(self)
        self.settings = Setting()
        self.timer = ""
        self.board = []
        self.buttons = []
        # This "fake" image fixes button size to pixels instead of text
        self.image = tk.PhotoImage(width=0, height=1)

    # adds minesweeper buttons
    def start_game(self, size):
        self.board = MinesweeperBoard(self.settings.board_size[size], self.settings.board_size[size])
        self.timer = Timer(self.root)
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
        self.buttons[row][col].config(
            text=self.board.buttons[row][col].value, state=tk.DISABLED,
            relief=tk.RIDGE, disabledforeground="#000000")

        if self.board.buttons[row][col].value == " ":
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if self.board.rows > row+i >= 0 \
                            and self.board.columns > col+j >= 0 \
                            and self.board.buttons[row+i][col+j].value != "X" \
                            and self.buttons[row+i][col+j]["state"] != tk.DISABLED:
                        self.buttons[row+i][col+j].config(
                            text=self.board.buttons[row+i][col+j].value,
                            state=tk.DISABLED, relief=tk.RIDGE, disabledforeground="#000000")
                        self.reveal_buttons((row+i), (col+j))
        self.game_status_check(row, col)

    # Checks the state of game.
    def game_status_check(self, row, col):
        if self.board.buttons[row][col].value == "X":
            self.buttons[row][col].config(bg=self.settings.colors["mine"])
            self.end_game("lost")
        else:
            bombs_remaining = len(self.buttons) * len(self.buttons[0]) // 10
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

    # Triggers different things depending on condition
    def end_game(self, end_condition):
        self.timer.isActive = False

        if end_condition == "won":
            for row in self.buttons:
                for button in row:
                    if button["state"] != tk.DISABLED:
                        button.config(bg=self.settings.colors["victory"])
            self.disable_all_buttons()
            self.check_highscore()
        elif end_condition == "lost":
            self.disable_all_buttons()
        elif end_condition == "quit":
            for row in range(self.board.rows):
                for col in range(self.board.columns):
                    self.buttons[row][col].destroy()
            self.buttons = []
            self.timer.time_label.destroy()
            self.root.main_menu_mode()

    # Checks if current time score is lower then top 3 highscore.
    def check_highscore(self):
        scores = self.score.fetch_by_size(self.root.size_button.get().lower())
        if len(scores) < 3:
            self.root.minesweeper_highscore_mode()
            return
        for score in scores:
            if self.timer.time < score[2]:
                self.root.minesweeper_highscore_mode()
                break

    # Disables all minesweeper buttons
    def disable_all_buttons(self):
        for row in range(self.board.rows):
            for col in range(self.board.columns):
                self.buttons[row][col].config(state=tk.DISABLED, disabledforeground="#000000")