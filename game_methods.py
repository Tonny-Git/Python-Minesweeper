import pygame


def draw_board(window, board):
    for i in range(board.rows):
        for j in range(board.columns):
            pygame.draw.rect(window, board.buttons[i][j].color,
                             (board.buttons[i][j].x, board.buttons[i][j].y,
                              board.buttons[i][j].width, board.buttons[i][j].height))
    pygame.display.update()
