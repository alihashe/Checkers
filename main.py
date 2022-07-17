import pygame
from Base.constants import SQUARE_SIZE, WIDTH, HEIGHT, RED
from Base.board import Board
from Base.game import Game

FPS = 60

WIND = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_from_mouse(pos):
    """Receives directions for moving a piece from the mouse."""
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIND)

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_from_mouse(pos)
                game.select(row, col)
                


        game.update()

    pygame.quit()

main()