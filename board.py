import pygame
from constant import *
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
    def draw(self):
        # draw lines
        for i in range(1, 9):
            pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                             (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        # draw vertical lines
        for i in range(1, 9):
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
pygame.init()
screen = pygame.display.set_mode((540, 540))
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