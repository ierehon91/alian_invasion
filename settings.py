class Settings:
    """Класс для хранения всех настроек игры Alien Invasion"""
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (40, 40, 40)

        # Настройка коробля
        self.ship_horizon_speed = 1.6
        self.ship_vertical_speed = 0.4

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (160, 160, 160)
        self.bullet_allowed = 4
