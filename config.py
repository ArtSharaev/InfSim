# ГЛАВНЫЕ НАСТРОЙКИ ------------------------------------------------------------
DIMENSIONS = (1000, 1000)  # размеры окна в пкс
HEALTHY_MICROBES_COUNT = 199  # количество здоровых микробов
INFECTED_MICROBES_COUNT = 1  # количество зараженных микробов
INFECTION_ZONE = 25  # зона заражения в пкс
INFECTION_CHANCE = 30  # вероятность заражения в процентах
DEATH_CHANCE = 70  # шанс смерти зараженного микроба (иначе - выздоровление)
TIME_BEFORE_DEATH = 7  # смерть зараженного микроба через (0 чтобы отключить)
ISOLATION_ZONE = 0  # зона изоляции для здоровых микробов в пкс (0-выкл)
SHOW_ISOLATION_ZONE = 1  # показывать зону изоляции (1-вкл, 0-выкл)
FPS = 120  # скорость симуляции

# ТЕХНИЧЕСКОЕ ------------------------------------------------------------------
MICROBE_SIZE = 7  # диаметр микроба в пкс
RMM = [-4, -3, -2, -1, 1, 2, 3, 4]  # random microbe movement,
# или случайное значение скорости передвижения по осям в пкс

# ЦВЕТА ------------------------------------------------------------------------
BG_COLOR = (17, 23, 40)
HEALTHY_MICROBE_COLOR = (0, 255, 128)
INFECTED_MICROBE_COLOR = (255, 128, 0)
OTHER_COLOR = (76, 187, 123)
