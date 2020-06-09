import tkinter as tk

from minesweeper_board import MinesweeperBoard


class Menu:

    def __init__(self, root):
        self.root = root
        self.button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_menu()
        self.board = []
        # This image fixes button size to pixels instead of text
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
            for j in range(self.board.columns):
                button = tk.Button(self.root, image=self.image, bg=self.board.buttons[i][j].color,
                                   width=22, height=22, text=" ", compound="c")
                button.config(command=lambda btn=button, board_btn=self.board.buttons[i][j]: self.push_button(btn, board_btn))
                button.place(x=self.board.buttons[i][j].x, y=self.board.buttons[i][j].y)

    def push_button(self, button, board_button):
        button.config(text=board_button.value, state=tk.DISABLED)





"""
def text_objects(text):
    font = pygame.font.Font('freesansbold.ttf', 16)
    text_surface = font.render(text, True, (40, 40, 40))
    return text_surface, text_surface.get_rect()


def draw_button(text, window, x, y):
    pygame.draw.rect(window, (200, 255, 255), (x, y, 60, 30))
    text_surface, text_rectangle = text_objects(text)
    text_rectangle.center = (x + (60/2), y + (30/2))
    window.blit(text_surface, text_rectangle)



def start_menu(root):
    
    window = pygame.display.set_mode((500, 500))
    pygame.draw.rect(window, (255, 255, 255), (0, 0, 500, 500))
    draw_button("Hello world", window, 30, 30)
    pygame.display.update()
    return window
    
    frame = tk.Frame(root, height=500, width=500, bg="white").pack()
    button = tk.Button(frame, text="Start Game", command=start_game).place(relx=0.45, rely=0.5)

    # pygame.draw.rect(window, (255, 255, 255), (0, 0, 500, 500))
    # draw_button("Hello world", window, 30, 30)
    # pygame.display.update()
    return root
"""
