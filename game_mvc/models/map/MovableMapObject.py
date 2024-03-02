from abc import ABC

from models.map.MapObject import MapObject
from models.map.MovableObjectDirection import (
    MovableObjectDirection,
    MovableObjectDirections
)

class MovableMapObject(MapObject, ABC):
    def __init__(self,  position, direction=MovableObjectDirections.UP, velocity=1):
        super().__init__(position)
        self.__direction = direction
        self.__velocity = velocity
        self.color = 'blue'

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

    def move(self, position):
        self.position = position
    
    def __str__(self):
        return super().__str__()