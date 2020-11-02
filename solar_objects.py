# coding: utf-8
# license: GPLv3



class Object:
    def __init__(self, m, x, y, Vx, Vy, Fx, Fy, R, color, image):

        self.m = m
        """Масса объекта"""

        self.x = x
        """Координата по оси **x**"""

        self.y = y
        """Координата по оси **y**"""

        self.Vx = Vx
        """Скорость по оси **x**"""

        self.Vy = Vy
        """Скорость по оси **y**"""

        self.Fx = Fx
        """Сила по оси **x**"""

        self.Fy = Fy
        """Сила по оси **y**"""

        self.R = R
        """Радиус объекта"""

        self.color = color
        """Цвет объекта"""

        self.image = image
        """Изображение объекта"""


class Planet(Object):
    """Тип данных, описывающий планету"""
    def __init__(self, m, x, y, Vx, Vy, Fx, Fy, R, color, image):

        super.__init__(m, x, y, Vx, Vy, Fx, Fy, R, color, image)
        """Параметры объекта"""

        self.type = "planet"
        """Признак объекта планеты"""


class Star(Object):
    """Тип данных, описывающий звезду"""
    def __init__(self, m, x, y, Vx, Vy, Fx, Fy, R, color, image):
        
        super.__init__(m, x, y, Vx, Vy, Fx, Fy, R, color, image)
        """Параметры объекта"""

        self.type = "star"
        """Признак объекта звезды"""

