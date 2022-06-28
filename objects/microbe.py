import pygame
from config import BG_COLOR


class Microbe:
    def __init__(self, dimensions, size, color, pos_x, pos_y, mov_x, mov_y):
        self.screen_dimensions = dimensions
        self.size = size
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mov_x = mov_x
        self.mov_y = mov_y

    def move(self, screen):
        pygame.draw.circle(screen, BG_COLOR,
                           (self.pos_x, self.pos_y), self.size // 2)
        # ось x
        if self.pos_x < 0 or self.pos_x > self.screen_dimensions[0]:
            self.mov_x = -self.mov_x
        self.pos_x += self.mov_x
        # ось y
        if self.pos_y < 0 or self.pos_y > self.screen_dimensions[0]:
            self.mov_y = -self.mov_y
        self.pos_y += self.mov_y
        self.render(screen)

    def render(self, screen):
        pygame.draw.circle(screen, self.color,
                           (self.pos_x, self.pos_y), self.size // 2)