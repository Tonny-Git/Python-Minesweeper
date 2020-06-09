import tkinter as tk

from minesweeper_board import MinesweeperBoard


class Menu:

    def __init__(self, root):
        self.root = root
        self.button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_menu()
        self.board = []
        self.buttons = []
        # This "fake" image fixes button size to pixels instead of text
        self.image = tk.PhotoImage(width=1, height=1)

    def start_menu(self):
        self.button.place(relx=0.45, rely=0.5)

    # removes start button and adds minesweeper buttons
    def start_game(self):
        self.button.place_forget()
        self.board = MinesweeperBoard(10, 10)
        # x = 0
        # y = 0
        for i in range(self.board.rows):
            temp_buttons = []
            for j in range(self.board.columns):
                button = tk.Button(self.root, image=self.image, bg=self.board.buttons[i][j].color,
                                   width=22, height=22, text=" ", compound="c")
                button.config(command=lambda btn=button, board_btn=self.board.buttons[i][j], row=i, col=j: self.reveal_buttons(row, col))
                button.place(x=self.board.buttons[i][j].x, y=self.board.buttons[i][j].y)
                temp_buttons.append(button)
            self.buttons.append(temp_buttons)

    def push_button(self, button, board_button):
        button.config(text=board_button.value, state=tk.DISABLED, relief=tk.RIDGE, disabledforeground="#000000")
        print(button["state"] == tk.DISABLED)

    def reveal_buttons(self, row, col):
        self.buttons[row][col].config(text=self.board.buttons[row][col].value, state=tk.DISABLED, relief=tk.RIDGE, disabledforeground="#000000")

        if self.board.buttons[row][col].value == " ":
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if 10 > row+i >= 0 and 10 > col+j >= 0 and self.board.buttons[row+i][col+j].value != "X" and self.buttons[row+i][col+j]["state"] != tk.DISABLED:
                        self.buttons[row+i][col+j].config(text=self.board.buttons[row+i][col+j].value, state=tk.DISABLED, relief=tk.RIDGE, disabledforeground="#000000")
                        self.reveal_buttons((row+i), (col+j))


    # reference, remove later!
    def button_value(self, bombs, buttons):
        for num in bombs:
            row = num // 10
            col = num % 10
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if 10 > row+i >= 0 and 10 > col+j >= 0 and buttons[row+i][col+j].value != "X":
                        if buttons[row+i][col+j].value == " ":
                            buttons[row+i][col+j].value = 1
                        else:
                            buttons[row+i][col+j].value += 1