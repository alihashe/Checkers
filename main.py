import pygame
from Base.constants import SQUARE_SIZE, WIDTH, HEIGHT
from Base.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
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
    board = Board()

    piece = board.pick_piece(0,1)

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_from_mouse(pos)
                piece = board.pick_piece(row, col)
                board.move(piece, 4, 3)

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

main()