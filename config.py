# ГЛАВНЫЕ НАСТРОЙКИ ------------------------------------------------------------
DIMENSIONS = (600, 600)  # размеры окна в пкс
HEALTHY_MICROBES_COUNT = 100  # количество здоровых микробов
INFECTED_MICROBES_COUNT = 1  # количество зараженных микробов
INFECTION_ZONE = 10  # зона заражения в пкс
INFECTION_CHANCE = 60  # вероятность заражения в процентах
DEATH_CHANCE = 70  # шанс смерти зараженного микроба (иначе - выздоровление)
TIME_BEFORE_DEATH = 4  # смерть зараженного микроба через (0 чтобы отключить)
ISOLATION_ZONE = 0  # зона изоляции для здоровых микробов в пкс (0-выкл)
SHOW_ISOLATION_ZONE = 0  # показывать зону изоляции (1-вкл, 0-выкл)
FPS = 120  # скорость симуляции

# ТЕХНИЧЕСКОЕ ------------------------------------------------------------------
MICROBE_SIZE = 7  # диаметр микроба в пкс
RMM = [-4, -3, -2, -1, 1, 2, 3, 4]  # random microbe movement
# или случайное значение скорости передвижения по осям в пкс

# ЦВЕТА ------------------------------------------------------------------------
BG_COLOR = (0, 0, 0)
HEALTHY_MICROBE_COLOR = (0, 255, 0)
INFECTED_MICROBE_COLOR = (255, 0, 0)
OTHER_COLOR = (76, 187, 123)
