from objects.microbe import Microbe
from config import HEALTHY_MICROBE_COLOR


class HealthyMicrobe(Microbe):
    def __init__(self, dimensions, size, pos_x, pos_y, mov_x, mov_y,
                 was_infected=False):
        color = HEALTHY_MICROBE_COLOR
        super().__init__(dimensions, size, color, pos_x, pos_y, mov_x, mov_y)
        self.was_infected = was_infected
