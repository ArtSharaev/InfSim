from random import randrange, choice
import datetime as dt
from objects.microbe import Microbe
from objects.microbes.healthy_microbe import HealthyMicrobe
from config import *


class InfectedMicrobe(Microbe):
    def __init__(self, dimensions, size, pos_x, pos_y, mov_x, mov_y):
        color = INFECTED_MICROBE_COLOR
        super().__init__(dimensions, size, color, pos_x, pos_y, mov_x, mov_y)
        self.microbes_in_my_zone = []  # список микробов в моей зоне заражения
        self.born_time = dt.datetime.now().second

    def infect(self, screen, microbes_list,
               healthy_microbes_list, infected_microbes_list):
        """Попытка заразить кого-нибудь"""
        for microbe in healthy_microbes_list:
            if ((abs(microbe.pos_x - self.pos_x) <= INFECTION_ZONE and
                 abs(microbe.pos_y - self.pos_y) <= INFECTION_ZONE) and
                    (microbe not in self.microbes_in_my_zone)):
                rr = randrange(1, 101)
                # вероятность заражения у переболевшего в 2 раза меньше
                if ((rr <= INFECTION_CHANCE and
                     not microbe.was_infected) or
                        (rr <= (INFECTION_CHANCE // 2) and
                         microbe.was_infected)):  # заразили

                    # удаляем здоровый микроб с поля
                    microbe.iz_rect_color = BG_COLOR
                    microbe.render(screen)
                    microbes_list.remove(microbe)
                    healthy_microbes_list.remove(microbe)

                    # вместо здорового создаем зараженный
                    inf_microbe = InfectedMicrobe(DIMENSIONS, MICROBE_SIZE,
                                                  microbe.pos_x,
                                                  microbe.pos_y,
                                                  microbe.mov_x, microbe.mov_y)
                    if ISOLATION_ZONE:
                        inf_microbe.max_pos_x = microbe.max_pos_x
                        inf_microbe.max_pos_y = microbe.max_pos_y
                        inf_microbe.min_pos_x = microbe.min_pos_x
                        inf_microbe.min_pos_y = microbe.min_pos_y
                        if SHOW_ISOLATION_ZONE:
                            inf_microbe.iz_rect_coords = microbe.iz_rect_coords
                    microbes_list.append(inf_microbe)
                    infected_microbes_list.append(inf_microbe)
                else:  # не заразили
                    self.microbes_in_my_zone.append(microbe)

            if ((abs(microbe.pos_x - self.pos_x) >= INFECTION_ZONE and
                 abs(microbe.pos_y - self.pos_y) >= INFECTION_ZONE) and
                    (microbe in self.microbes_in_my_zone)):
                # если микроб покинул нашу зону заражения
                self.microbes_in_my_zone.remove(microbe)

    def try_die_or_recovery(self, screen, microbes_list,
                            healthy_microbes_list,
                            infected_microbes_list):
        """По окончании своего времени
        микроб может может выздороветь или умереть"""
        if TIME_BEFORE_DEATH > 0:
            if dt.datetime.now().second - self.born_time \
                    >= TIME_BEFORE_DEATH:
                # удаляем микроб с поля
                self.color = BG_COLOR
                self.iz_rect_color = BG_COLOR
                self.render(screen)
                microbes_list.remove(self)
                infected_microbes_list.remove(self)
                if randrange(1, 101) <= DEATH_CHANCE:  # умер
                    pass
                else:  # выздоровел
                    # на месте нашего создаем здорового
                    h_microbe = HealthyMicrobe(DIMENSIONS, MICROBE_SIZE,
                                               self.pos_x,
                                               self.pos_y,
                                               self.mov_x, self.mov_y,
                                               was_infected=True)
                    if ISOLATION_ZONE:
                        h_microbe.max_pos_x = self.max_pos_x
                        h_microbe.max_pos_y = self.max_pos_y
                        h_microbe.min_pos_x = self.min_pos_x
                        h_microbe.min_pos_y = self.min_pos_y
                        if SHOW_ISOLATION_ZONE:
                            h_microbe.iz_rect_coords = self.iz_rect_coords
                    microbes_list.append(h_microbe)
                    healthy_microbes_list.append(h_microbe)
