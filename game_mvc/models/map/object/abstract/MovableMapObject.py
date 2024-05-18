from abc import ABC

from .. import MapObject
from ..MapObjectDirection import MapObjectDirection, UP


class MovableMapObject(MapObject, ABC):
    def __init__(self, position, size, direction=None, velocity=None):
        super().__init__(position, size)
        self.__direction = direction or UP
        self.__velocity = velocity or 1
        self.color = 'blue'
        self.is_movable = True

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        self.__velocity = velocity

    @property
    def direction(self) -> MapObjectDirection:
        return self.__direction

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @property
    def image(self):
        return self._image + '_' + self.__direction.string

    @image.setter
    def image(self, image):
        self._image = image

    def __str__(self):
        return super().__str__()
