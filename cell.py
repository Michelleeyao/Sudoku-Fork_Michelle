import pygame
from constant import *

pygame.init()

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch = 0
        self.selected = False
        self.width = 60
        self.height = 60
        self.locked = False
        self.last_clicked = False
        if self.value != 0:
            self.locked = True
        else:
            self.locked = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketch = value

    def draw(self):
        font = pygame.font.Font(None, 50)
        num_surf = font.render(str(self.value), 0, (0, 255, 0))

        x = self.col * self.width
        y = self.row * self.height

        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        # Check mouse position and click on cell
        if pygame.Rect(x, y, self.width, self.height).collidepoint(pos):
            if click and not self.last_clicked:
                self.selected = not self.selected
            self.last_clicked = click

        if self.value != '0':
            num_rect = num_surf.get_rect(center = (x + self.width // 2, y + self.height // 2))
            self.screen.blit(num_surf, num_rect)

        if self.selected:
            pygame.draw.rect(self.screen, RED, pygame.Rect(x, y, self.width, self.height), 5)

        if self.value == '0':
            font = pygame.font.Font(None, 30)
            key = pygame.key.get_pressed()
            val = None
            if key == pygame.K_1:
                val = '1'
            elif key == pygame.K_2:
                val = '2'
            elif key == pygame.K_3:
                val = '3'
            elif key == pygame.K_4:
                val = '4'
            elif key == pygame.K_5:
                val = '5'
            elif key == pygame.K_6:
                val = '6'
            elif key == pygame.K_7:
                val = '7'
            elif key == pygame.K_8:
                val = '8'
            elif key == pygame.K_9:
                val = '9'

            num_surf = font.render(str(val), 0, GREY)
            num_rect = num_surf.get_rect(center = (x + self.width // 4, y + self.height // 4))
            self.screen.blit(num_surf, num_rect)

# test

"""
screen = pygame.display.set_mode((WIDTH, HEIGHT))

a = Cell('-', 4, 4, screen)
b = Cell('5', 2, 2, screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    a.draw()
    b.draw()
    pygame.display.update()

pygame.quit()
"""