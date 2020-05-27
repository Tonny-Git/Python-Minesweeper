import pygame

from minesweeper_button import MinesweeperButton

pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

button = MinesweeperButton(5, 5)

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(window, (212, 213, 214), (button.x, button.y, button.width, button.height))
    pygame.display.update()

pygame.quit()
