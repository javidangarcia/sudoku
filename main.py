import pygame
from sudoku.board import Board
from sudoku.constants import *

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

def main():
    board = Board(ROWS, COLS)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                clicked = board.click(position)
                if clicked:
                    board.select(clicked[0], clicked[1])
        
        WINDOW.fill(WHITE)
        board.draw_board(WINDOW)
        pygame.display.update()
            
main()
pygame.quit()
    