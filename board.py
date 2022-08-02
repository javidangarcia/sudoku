import pygame
from constants import *
from slots import Slot

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.width = WIDTH
        self.height = HEIGHT
        self.slots = []
        for row in range(rows):
            slots = []
            for col in range(cols):
                slots.append(Slot(board[row][col], row, col, self.width, self.height))
            self.slots.append(slots)
            

    def draw_board(self, window):
        gap = self.width / 9
        for row in range(self.rows):
            if row % 3 == 0 and row != 0:
                width = 4
            else:
                width = 1
            pygame.draw.line(window, BLACK, (0, row * gap), (self.width, row * gap), width)
            pygame.draw.line(window, BLACK, (row * gap, 0), (row * gap, self.height), width)

        for row in range(self.rows):
            for col in range(self.cols):
                self.slots[row][col].draw_slot(window)



