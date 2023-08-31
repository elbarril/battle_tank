from MovableMapObject import MovableMapObject
from Direction import Direction

class Bullet(MovableMapObject):
    __width = __height = 1
    __image_url = 'bullet.png'
    def __init__(self, row:int, column:int, direction:Direction, map_object:MovableMapObject):
        super().__init__(row, column, self.__width, self.__height, self.__image_url)
        self.direction = direction
        self.creator = map_object