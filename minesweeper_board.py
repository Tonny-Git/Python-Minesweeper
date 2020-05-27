from minesweeper_button import MinesweeperButton


class MinesweeperBoard:

    def __init__(self, columns, rows):
        self.rows = rows
        self.columns = columns
        self.buttons = self.create_board()

    def create_board(self):
        buttons = []
        x = 5
        y = 5
        for i in range(self.rows):
            temp_buttons = []
            for j in range(self.columns):
                button = MinesweeperButton((x + (j * 30)), (y + (i * 30)))
                temp_buttons.append(button)
            buttons.append(temp_buttons)
        return buttons
