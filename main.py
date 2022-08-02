import pygame
from board import Board
from constants import *

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

def main():
    board = Board(ROWS, COLS)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        WINDOW.fill(WHITE)
        board.draw_board(WINDOW)
        pygame.display.update()
            
main()
pygame.quit()
    