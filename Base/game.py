import pygame
from .constants import BLUE, RED, SQUARE_SIZE, WHITE
from Base.board import Board



class Game:
    def __init__(self, wind):
        self._init()
        self.wind = wind

    def update(self):
        """Updates the board after a move."""
        self.board.draw(self.wind)
        self.show_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        """Private function for initialization. (USE reset( ) INSTEAD)"""
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def reset(self):
        """Restarts the game."""
        self._init()

    def select(self, row, col):
        """Makes a piece "selected" and sets up possible movement."""
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.pick_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.find_valid_moves(piece)
                return True
        
        return False

    def _move(self, row, col):
        """Private function for movement."""
        piece = self.board.pick_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        
        return True

    def show_valid_moves(self, moves):
        """Creates a visual display for the moves of a certain piece."""
        for move in moves:
            row, col = move
            pygame.draw.circle(self.wind, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        """Switches turn between players."""
        if self.turn == RED:
            self.turn == WHITE
        else:
            self.turn == RED