class Settings:
    """Класс для хранения всех настроек игры Alien Invasion"""
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1250
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        # настройки корабля
        self.ship_speed = 0.3
        self.ship_limit = 3
        # параметры снаряда
        self.bullet_speed = 0.7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4
        # Настройки пришельцев

        self.fleet_drop_speed = 15
        self.speedup_scale = 1.2
        self.score_scale = 2
        self.initialize_dynamic_settings()
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.alien_speed = 0.3
        # fleet_direction = 1 обозначает движение вправо, -1 влево
        # подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        self.alien_points *= self.score_scale
