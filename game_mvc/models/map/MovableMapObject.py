from abc import ABC

from models.map.MapObject import MapObject
from models.map.MovableObjectDirection import (
    MovableObjectDirection,
    MovableObjectDirections
)

class MovableMapObject(MapObject, ABC):
    def __init__(self,  position, direction=MovableObjectDirections.UP):
        super().__init__(position)
        self.__direction = direction

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