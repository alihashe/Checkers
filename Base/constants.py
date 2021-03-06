import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# IN RGB
RED = (255, 0, 0)
LIGHTRED = (250, 70, 60)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# Images
CROWN = pygame.transform.scale(pygame.image.load('assets/checker_crown_01.png'), (50, 40))