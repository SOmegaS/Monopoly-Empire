"""
Стартовый скрипт для работы с pygame
"""

import sys
import pygame as pg


class Object:
    """Класс объекта с необходимыми переменными"""

    def __init__(self):
        # Изображения
        field_img = pg.image.load('images/field.jpg')
        self.images = {
            'player_cocacola': pg.image.load('images/cocacola.png'),
            'player_headfones': pg.image.load('images/headfones.png'),
            'player_joystick': pg.image.load('images/joystick.png'),
            'player_car': pg.image.load('images/car.png'),
            'field': field_img,
            'nerf': field_img.subsurface((759, 887, 60, 60)),
            'transformers': field_img.subsurface((592, 887, 60, 60)),
            'spotify': field_img.subsurface((428, 887, 60, 60)),
            'beats': field_img.subsurface((264, 887, 60, 60)),
            'fender': field_img.subsurface((180, 887, 60, 60)),
            'jetblue': pg.transform.rotate(field_img.subsurface((50, 760, 60, 60)), 90),
            'ea': pg.transform.rotate(field_img.subsurface((50, 677, 60, 60)), 90),
            'electricity': pg.transform.rotate(field_img.subsurface((50, 594, 60, 60)), 90),
            'hasbro': pg.transform.rotate(field_img.subsurface((50, 512, 60, 60)), 90),
            'under_armour': pg.transform.rotate(field_img.subsurface((50, 430, 60, 60)), 90),
            'carnival': pg.transform.rotate(field_img.subsurface((50, 265, 60, 60)), 90),
            'yahoo': pg.transform.rotate(field_img.subsurface((50, 183, 60, 60)), 90),
            'paramount': pg.transform.rotate(field_img.subsurface((182, 52, 60, 60)), 180),
            'chevrolet': pg.transform.rotate(field_img.subsurface((264, 52, 60, 60)), 180),
            'ebay': pg.transform.rotate(field_img.subsurface((428, 52, 60, 60)), 180),
            'xgames': pg.transform.rotate(field_img.subsurface((510, 52, 60, 60)), 180),
            'ducati': pg.transform.rotate(field_img.subsurface((675, 52, 60, 60)), 180),
            'mcdonalds': pg.transform.rotate(field_img.subsurface((759, 52, 60, 60)), 180),
            'intel': pg.transform.rotate(field_img.subsurface((887, 183, 60, 60)), -90),
            'xbox': pg.transform.rotate(field_img.subsurface((887, 265, 60, 60)), -90),
            'water': pg.transform.rotate(field_img.subsurface((887, 347, 60, 60)), -90),
            'nestle': pg.transform.rotate(field_img.subsurface((887, 430, 60, 60)), -90),
            'samsung': pg.transform.rotate(field_img.subsurface((887, 594, 60, 60)), -90),
            'cocacola': pg.transform.rotate(field_img.subsurface((887, 760, 60, 60)), -90),
            'upper_left_corner': field_img.subsurface((170, 170, 333, 333)),
            'lower_left_corner': field_img.subsurface((170, 500, 333, 333)),
            'top_right_corner': field_img.subsurface((500, 170, 333, 333)),
            'bottom_right_corner': field_img.subsurface((500, 500, 333, 333)),
        }


class Player(Object):
    """Класс игрока"""

    def __init__(self, corner, chip):
        super().__init__()
        # Деньги
        self.money = 1000
        # Бренды в собственности
        self.brands = []
        # Угол с башней
        self.corner = corner
        # Является ли банкротом
        self.bankrupt = False
        # Фишка игрока
        self.chip = chip
        # Координата
        self.coord = 0

    def draw_tower(self, size):
        """Отрисовка башни игрока"""
        # Размер поверхности
        size = min(size) // 3, min(size) // 3
        # Создание поверхности
        surf = pg.Surface(size)
        # Фоновое изображение
        surf.blit(pg.transform.scale(self.images[self.corner], size), (0, 0))
        # Надпись
        surf.blit(pg.font.SysFont('arial', 36).render(f'Игрок {self.chip}: {self.money}$',
                                                      True, (255, 0, 0)), (0, 0))
        # Бренды
        for key, val in enumerate(self.brands):
            surf.blit(pg.transform.scale(self.images[val],
                                         (60 * min(size) // 333, 60 * min(size) // 333)),
                      (key % 5 * 60 * min(size) / 333,
                       key // 5 * 60 * min(size) / 333 + 40 * min(size) / 333))
        return surf

    def draw(self, screen):
        """Отрисовка фишки игрока"""
        # Нижняя полоса
        if 0 <= self.coord < 9:
            screen.blit(pg.transform.scale(self.images[self.chip],
                                           (min(screen.get_size()) // 10,
                                            min(screen.get_size()) // 10)),
                        (((10 - self.coord % 9) * 83 - 10) * min(screen.get_size()) // 1000,
                         840 * min(screen.get_size()) // 1000))
        # Левая полоса
        elif 9 <= self.coord < 18:
            screen.blit(pg.transform.scale(self.images[self.chip],
                                           (min(screen.get_size()) // 10,
                                            min(screen.get_size()) // 10)),
                        (25 * min(screen.get_size()) // 1000,
                         ((10 - self.coord % 9) * 83 - 10) * min(screen.get_size()) // 1000))
        # Верхняя полоса
        elif 18 <= self.coord < 27:
            screen.blit(pg.transform.scale(self.images[self.chip],
                                           (min(screen.get_size()) // 10,
                                            min(screen.get_size()) // 10)),
                        ((self.coord % 9 * 83 + 75) * min(screen.get_size()) // 1000,
                         25 * min(screen.get_size()) // 1000))
        # Правая полоса
        elif 27 <= self.coord < 36:
            screen.blit(pg.transform.scale(self.images[self.chip],
                                           (min(screen.get_size()) // 10,
                                            min(screen.get_size()) // 10)),
                        (860 * min(screen.get_size()) // 1000,
                         (self.coord % 9 * 83 + 75) * min(screen.get_size()) // 1000))


class Bank:
    """Класс банка"""

    def __init__(self):
        # Стоимости брендов
        self.prices = {
            'jetblue': 150,
            'ea': 150,
            'electricity': 150,
            'hasbro': 150,
            'under_armour': 200,
            'carnival': 200,
            'yahoo': 200,
            'paramount': 250,
            'chevrolet': 250,
            'ebay': 250,
            'xgames': 300,
            'ducati': 300,
            'mcdonalds': 300,
            'intel': 350,
            'xbox': 350,
            'water': 150,
            'nestle': 350,
            'samsung': 400,
            'cocacola': 400,
        }
        # Владельцы брендов
        self.owners = {
            'jetblue': 'bank',
            'ea': 'bank',
            'electricity': 'bank',
            'hasbro': 'bank',
            'under_armour': 'bank',
            'carnival': 'bank',
            'yahoo': 'bank',
            'paramount': 'bank',
            'chevrolet': 'bank',
            'ebay': 'bank',
            'xgames': 'bank',
            'ducati': 'bank',
            'mcdonalds': 'bank',
            'intel': 'bank',
            'xbox': 'bank',
            'water': 'bank',
            'nestle': 'bank',
            'samsung': 'bank',
            'cocacola': 'bank',
        }


class Main(Object):
    """Главный класс"""

    def __init__(self):
        # Инициализация
        super().__init__()
        pg.init()
        self.screen = pg.display.set_mode((1000, 1000), pg.RESIZABLE)
        self.clock = pg.time.Clock()

        # Массив игроков
        self.players = [
            Player('upper_left_corner', 'player_cocacola'),
            Player('top_right_corner', 'player_headfones'),
            Player('lower_left_corner', 'player_joystick'),
            Player('bottom_right_corner', 'player_car'),
        ]

        # Главный цикл
        while True:
            # Обработка событий
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            # Отрисовка кадра
            # Отрисовка поля
            tmp_size = (min(self.screen.get_size()), min(self.screen.get_size()))
            tmp_img = pg.transform.scale(self.images['field'], tmp_size)
            self.screen.blit(tmp_img, tmp_img.get_rect())

            # Отрисовка башен игроков
            self.screen.blit(self.players[0].draw_tower(self.screen.get_size()),
                             (min(self.screen.get_size()) / 100 * 17,
                              min(self.screen.get_size()) / 100 * 17))
            self.screen.blit(self.players[1].draw_tower(self.screen.get_size()),
                             (min(self.screen.get_size()) / 2,
                              min(self.screen.get_size()) / 100 * 17))
            self.screen.blit(self.players[2].draw_tower(self.screen.get_size()),
                             (min(self.screen.get_size()) / 100 * 17,
                              min(self.screen.get_size()) / 2))
            self.screen.blit(self.players[3].draw_tower(self.screen.get_size()),
                             (min(self.screen.get_size()) / 2,
                              min(self.screen.get_size()) / 2))

            # Отрисовка игроков
            self.players[0].draw(self.screen)
            self.players[1].draw(self.screen)
            self.players[2].draw(self.screen)
            self.players[3].draw(self.screen)

            # Отладка чтобы координата менялась, можно удалить
            self.players[0].coord = pg.time.get_ticks() // 1000 % 36
            self.players[1].coord = pg.time.get_ticks() // 1000 % 36 + 1
            self.players[2].coord = pg.time.get_ticks() // 1000 % 36 + 2
            self.players[3].coord = pg.time.get_ticks() // 1000 % 36 + 3

            # Подтверждение отрисовки и ожидание
            pg.display.flip()
            self.clock.tick(60)  # FPS


if __name__ == '__main__':
    Main()
