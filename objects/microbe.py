import pygame
from config import BG_COLOR, ISOLATION_ZONE, SHOW_ISOLATION_ZONE, OTHER_COLOR


class Microbe:
    def __init__(self, dimensions, size, color, pos_x, pos_y, mov_x, mov_y):
        self.screen_dimensions = dimensions
        self.size = size
        self.color = color
        self.iz_rect_color = OTHER_COLOR
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mov_x = mov_x
        self.mov_y = mov_y
        if SHOW_ISOLATION_ZONE:
            self.iz_rect_coords = (self.pos_x - ISOLATION_ZONE // 2,
                                   self.pos_y - ISOLATION_ZONE // 2,
                                   ISOLATION_ZONE, ISOLATION_ZONE)
        if ISOLATION_ZONE:
            self.min_pos_x = pos_x - ISOLATION_ZONE // 2
            self.max_pos_x = pos_x + ISOLATION_ZONE // 2

            self.min_pos_y = pos_y - ISOLATION_ZONE // 2
            self.max_pos_y = pos_y + ISOLATION_ZONE // 2

    def move(self, screen):
        pygame.draw.circle(screen, BG_COLOR,
                           (self.pos_x, self.pos_y), self.size // 2)
        # ось x
        if (self.pos_x < 0 or
                self.pos_x > self.screen_dimensions[0] or
                (ISOLATION_ZONE and self.pos_x < self.min_pos_x) or
                (ISOLATION_ZONE and self.pos_x > self.max_pos_x)):
            self.mov_x = -self.mov_x
        self.pos_x += self.mov_x
        # ось y
        if (self.pos_y < 0 or
                self.pos_y > self.screen_dimensions[1] or
                (ISOLATION_ZONE and self.pos_y < self.min_pos_y) or
                (ISOLATION_ZONE and self.pos_y > self.max_pos_y)):
            self.mov_y = -self.mov_y
        self.pos_y += self.mov_y
        self.render(screen)

    def render(self, screen):
        pygame.draw.circle(screen, self.color,
                           (self.pos_x, self.pos_y), self.size // 2)
        if SHOW_ISOLATION_ZONE:
            pygame.draw.rect(screen, self.iz_rect_color,
                             self.iz_rect_coords, 1)