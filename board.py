import pygame
from constant import *
from cell import Cell

pygame.init()

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        # andrew
        # sets a 2d list of cell objects correspondent to board size
        self.cells = [[Cell('-', i, j, self.screen) for i in range(10)] for j in range(10)]

    def draw(self):
        # draw lines
        for i in range(1, 9):
            # defined box lines horizontal
            if i % 3 == 0:
                pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                                 (WIDTH, SQUARE_SIZE * i), LINE_WIDTH * 2)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                                 (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        # draw vertical lines
        for i in range(1, 9):
            # defined box line vertical
            if i % 3 == 0:
                pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                                 (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH * 2)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                                 (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)
        """
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(self.screen)
                """
    def select(self, row, col):
        pass

    def click(self, x, y):
        pass
    def clear(self):
        pass
    def sketch(self, value):
        pass
    def place_number(self, value):
        pass
    def reset_to_original(self):
        pass
    def is_full(self):
        pass
    def update_board(self):
        pass
    def find_empty(self):
        pass
    def check_board(self):
        pass
#test

screen = pygame.display.set_mode((WIDTH, HEIGHT))

a = Board( 5, 1, screen, 5)
a1 = Cell('5', 1, 1, screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    a.draw()
    a1.draw()
    pygame.display.update()

pygame.quit()