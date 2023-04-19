import pygame

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
        num_surf = font.render(self.value, 0, (0,255,0))

        x = self.col * self.width
        y = self.row * self.height

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0),
                             pygame.Rect(self.col * 60, self.row * 60, 60, 60), 12)
            self.selected = False

        if self.value != 0:
            num_rect = num_surf.get_rect(
                center = (self.width // 2 + self.width * self.col, self.height // 2 + self.height * self.row))
            self.screen.blit(num_surf, num_rect)


screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))

a = Cell('6', 1, 1, screen)
a.draw()
