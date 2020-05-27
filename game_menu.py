import pygame


def text_objects(text):
    font = pygame.font.Font('freesansbold.ttf', 16)
    text_surface = font.render(text, True, (40, 40, 40))
    return text_surface, text_surface.get_rect()


def draw_button(text, window, x, y):
    pygame.draw.rect(window, (200, 255, 255), (x, y, 60, 30))
    text_surface, text_rectangle = text_objects(text)
    text_rectangle.center = (x + (60/2), y + (30/2))
    window.blit(text_surface, text_rectangle)


def start_menu():
    window = pygame.display.set_mode((500, 500))
    pygame.draw.rect(window, (255, 255, 255), (0, 0, 500, 500))
    draw_button("Hello world", window, 30, 30)
    pygame.display.update()
    return window
