from abc import ABC

from models.map.MapObject import MapObject
from models.map.MovableObjectDirection import (
    MovableObjectDirection,
    MovableObjectDirections
)

class MovableMapObject(MapObject, ABC):
    def __init__(self, position, size, direction=None, velocity=None):
        super().__init__(position, size)
        self.__direction = direction or MovableObjectDirections.UP
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
    def direction(self) -> MovableObjectDirection:
        return self.__direction
    
    @direction.setter
    def direction(self, direction):
        self.__direction = direction
    
    def __str__(self):
        return super().__str__()