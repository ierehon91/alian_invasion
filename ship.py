import pygame


class Ship():
    """Класс для управления кораблем"""
    def __init__(self, ai_game):
        """Инициализируем корабль и задаем его начальную позицию"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружаем изображение коробля и получаем прямоугольник
        self.image = pygame.image.load('images\\ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисуем корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)