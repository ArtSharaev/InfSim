import pygame
from random import choice, randrange
from objects.microbes.healthy_microbe import HealthyMicrobe
from objects.microbes.infected_microbe import InfectedMicrobe
from config import *

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('InfSim')
    clock = pygame.time.Clock()

    font_size = DIMENSIONS[1] // 20
    font = pygame.font.SysFont('arial.ttf', font_size)
    i_count_text_x = i_count_text_y = time_text_x = h_count_text_x = 0
    h_count_text_y = font_size - 10
    time_text_y = (font_size - 10) * 2

    screen = pygame.display.set_mode(DIMENSIONS)
    screen.fill(BG_COLOR)

    microbes = list()
    healthy_microbes = list()
    infected_microbes = list()

    for _ in range(HEALTHY_MICROBES_COUNT):  # создание здоровых микробов
        hm = HealthyMicrobe(DIMENSIONS, MICROBE_SIZE,
                            randrange(0, DIMENSIONS[0]),
                            randrange(0, DIMENSIONS[1]),
                            choice(RMM), choice(RMM))
        microbes.append(hm)
        hm.move(screen)
        healthy_microbes.append(hm)

    for _ in range(INFECTED_MICROBES_COUNT):  # создание заражённых микробов
        im = InfectedMicrobe(DIMENSIONS, MICROBE_SIZE,
                             randrange(0, DIMENSIONS[0]),
                             randrange(0, DIMENSIONS[1]),
                             choice(RMM), choice(RMM))
        microbes.append(im)
        infected_microbes.append(im)

    seconds = seconds_to_text = 0

    running = True
    infection_exist = True  # проверка того, что есть оба типа микробов
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for microbe in microbes:  # движение всех микробов
            microbe.move(screen)
        if infection_exist:
            for microbe in infected_microbes:  # проверки для заражённых
                microbe.infect(screen, microbes,
                               healthy_microbes, infected_microbes)
                microbe.try_die_or_recovery(screen, microbes,
                                            healthy_microbes,
                                            infected_microbes)

        # дичь со временем
        ticks = pygame.time.get_ticks()
        minutes = int(ticks / 60000 % 24)
        seconds = int(ticks / 1000 % 60) + minutes * 60
        millis = ticks % 1000

        if healthy_microbes and infected_microbes:
            seconds_to_text = seconds
        else:
            infection_exist = False

        # ох уж эти тексты -----------------------------------------------------
        i_count_text_surface = font.render(str(len(infected_microbes)),
                                           True, INFECTED_MICROBE_COLOR)
        i_count_surface = pygame.Surface(
            (i_count_text_surface.get_size()[0] + 100,
             i_count_text_surface.get_size()[1]))
        i_count_surface.fill(BG_COLOR)
        i_count_surface.blit(i_count_text_surface, pygame.Rect(0, 0, 10, 10))
        i_count_surface.set_alpha(50)
        screen.blit(i_count_surface, (i_count_text_x, i_count_text_y))

        h_count_text_surface = font.render(str(len(healthy_microbes)),
                                           True, HEALTHY_MICROBE_COLOR)
        h_count_surface = pygame.Surface(
            (h_count_text_surface.get_size()[0] + 100,
             h_count_text_surface.get_size()[1]))
        h_count_surface.fill(BG_COLOR)
        h_count_surface.blit(h_count_text_surface, pygame.Rect(0, 0, 10, 10))
        h_count_surface.set_alpha(50)
        screen.blit(h_count_surface, (h_count_text_x, h_count_text_y))

        time_text_surface = font.render(str(seconds_to_text),
                                        True, OTHER_COLOR)
        time_surface = pygame.Surface((time_text_surface.get_size()[0] + 100,
                                       time_text_surface.get_size()[1]))
        time_surface.fill(BG_COLOR)
        time_surface.blit(time_text_surface, pygame.Rect(0, 0, 10, 10))
        time_surface.set_alpha(50)
        screen.blit(time_surface, (time_text_x, time_text_y))
        # ----------------------------------------------------------------------
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()
