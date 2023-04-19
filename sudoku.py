import pygame
from constant import *
from cell import Cell
from board import Board
from sudoku_generator import SudokuGenerator
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))

a = Board( 5, 1, screen, 5)
a.draw()
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    a.draw()
    pygame.display.update()

pygame.quit()