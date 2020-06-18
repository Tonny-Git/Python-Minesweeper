import random

from Components.minesweeper_button import MinesweeperButton


class MinesweeperBoard:

    def __init__(self, columns, rows):
        self.rows = rows
        self.columns = columns
        self.buttons = self.create_board()

    # creates an 2:d array with minesweeper_buttons
    def create_board(self):
        bomb_pos = self.bomb_position()
        buttons = []
        x = 50
        y = 50
        for i in range(self.rows):
            temp_buttons = []
            for j in range(self.columns):
                if i*self.rows + j in bomb_pos:
                    button = MinesweeperButton((x + (j * 30)), (y + (i * 30)), "X")
                    temp_buttons.append(button)
                else:
                    button = MinesweeperButton((x + (j * 30)), (y + (i * 30)), " ")
                    temp_buttons.append(button)
            buttons.append(temp_buttons)
        self.button_value(bomb_pos, buttons)
        return buttons

    # Randomizes an array with unique numbers
    def bomb_position(self):
        bombs = []
        i = 0
        while i < (self.columns * self.rows // 10):
            num = random.randrange(0, self.columns * self.rows, 1)
            if num not in bombs:
                bombs.append(num)
                i += 1
        return bombs

    # Adds value to the buttons surrounding bombs
    def button_value(self, bombs, buttons):
        for num in bombs:
            row = num // self.rows
            col = num % self.columns
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if self.rows > row+i >= 0 and self.columns > col+j >= 0 and buttons[row+i][col+j].value != "X":
                        if buttons[row+i][col+j].value == " ":
                            buttons[row+i][col+j].value = 1
                        else:
                            buttons[row+i][col+j].value += 1
