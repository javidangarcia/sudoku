import pygame
from constants import *

class Slot:
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw_slot(self, window):
        pygame.init()
        FONT = pygame.font.SysFont("comicsans", 25)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            number = FONT.render(str(self.temp), 1, GRAY)
            window.blit(number, (x + 5, y + 5))
        elif self.value != 0:
            number = FONT.render(str(self.value), 1, BLACK)
            window.blit(number, (x + (gap / 2 - number.get_width() / 2), y + (gap / 2 - number.get_height() / 2)))
        
        if self.selected:
            pygame.draw.rect(window, RED, (x, y, gap, gap), 3)

    def set_value(self, value):
        self.value = value

    def set_temp(self, value):
        self.temp = value
