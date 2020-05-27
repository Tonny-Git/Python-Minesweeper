import pygame

from minesweeper_board import MinesweeperBoard

pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

board = MinesweeperBoard(10, 10)

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(board.rows):
        for j in range(board.columns):
            pygame.draw.rect(window, board.buttons[i][j].color,
                             (board.buttons[i][j].x, board.buttons[i][j].y,
                              board.buttons[i][j].width, board.buttons[i][j].height))
            pygame.display.update()
    # pygame.draw.rect(window, button.color, (button.x, button.y, button.width, button.height))
    # pygame.display.update()

pygame.quit()
