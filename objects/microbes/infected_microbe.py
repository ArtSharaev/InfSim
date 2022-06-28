from random import randrange, choice
import datetime as dt
from objects.microbe import Microbe
from objects.microbes.healthy_microbe import HealthyMicrobe
from config import *


class InfectedMicrobe(Microbe):
    def __init__(self, dimensions, size, pos_x, pos_y, mov_x, mov_y):
        color = INFECTED_MICROBE_COLOR
        super().__init__(dimensions, size, color, pos_x, pos_y, mov_x, mov_y)
        self.microbes_in_my_zone = []
        self.born_time = dt.datetime.now().second

    def infect(self, screen, microbes_list,
               healthy_microbes_list, infected_microbes_list):

        for microbe in healthy_microbes_list:
            if ((abs(microbe.pos_x - self.pos_x) <= INFECTION_ZONE and
                 abs(microbe.pos_y - self.pos_y) <= INFECTION_ZONE) and
                    (microbe not in self.microbes_in_my_zone)):
                rr = randrange(1, 101)
                if ((rr <= INFECTION_CHANCE and not microbe.was_infected) or
                        (rr <= (INFECTION_CHANCE // 2) and microbe.was_infected)):
                    # если микроб переболел, то вероятность повторно заразиться
                    # в 2 раза меньше
                    microbe.iz_rect_color = BG_COLOR
                    microbe.render(screen)
                    microbes_list.remove(microbe)
                    healthy_microbes_list.remove(microbe)

                    inf_microbe = InfectedMicrobe(DIMENSIONS, MICROBE_SIZE,
                                                  microbe.pos_x,
                                                  microbe.pos_y,
                                                  choice(RMM), choice(RMM))
                    microbes_list.append(inf_microbe)
                    infected_microbes_list.append(inf_microbe)
                else:
                    self.microbes_in_my_zone.append(microbe)
            if ((abs(microbe.pos_x - self.pos_x) >= INFECTION_ZONE and
                 abs(microbe.pos_y - self.pos_y) >= INFECTION_ZONE) and
                    (microbe in self.microbes_in_my_zone)):
                self.microbes_in_my_zone.remove(microbe)

    def try_to_die_or_recovery(self, screen, microbes_list,
                               healthy_microbes_list,
                               infected_microbes_list):
        if TIME_BEFORE_DEATH > 0:
            if dt.datetime.now().second - self.born_time \
                    >= TIME_BEFORE_DEATH:
                if randrange(1, 101) <= DEATH_CHANCE:  # умер
                    self.color = BG_COLOR
                    self.iz_rect_color = BG_COLOR
                    self.render(screen)
                    microbes_list.remove(self)
                    infected_microbes_list.remove(self)
                else:  # выздоровел
                    self.color = BG_COLOR
                    self.iz_rect_color = BG_COLOR
                    self.render(screen)
                    microbes_list.remove(self)
                    infected_microbes_list.remove(self)
                    h_microbe = HealthyMicrobe(DIMENSIONS, MICROBE_SIZE,
                                               self.pos_x,
                                               self.pos_y,
                                               choice(RMM), choice(RMM))
                    h_microbe.was_infected = True
                    microbes_list.append(h_microbe)
                    healthy_microbes_list.append(h_microbe)
