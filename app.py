import pygame

import game_menu as menu
import game_methods as gm
from minesweeper_board import MinesweeperBoard

pygame.init()

pygame.display.set_caption("Minesweeper")
# window = pygame.display.set_mode((500, 500))
window = menu.start_menu()
board = MinesweeperBoard(10, 10)

run = True
while run:
    pygame.time.delay(100)
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # gm.draw_board(window, board)

pygame.quit()