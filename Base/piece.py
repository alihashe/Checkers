import pygame
from .constants import RED, WHITE, GREY, SQUARE_SIZE

class Piece:
    PADDING = 12
    OUTLINE = 2


    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        """Places pieces in the middle of a square."""
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        """Turns ordinary piece into a king."""
        self.king = True

    def draw(self, wind):
        """Draws each individual piece."""
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(wind, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(wind, self.color, (self.x, self.y), radius)

    def __repr__(self):
        return str(self.color)