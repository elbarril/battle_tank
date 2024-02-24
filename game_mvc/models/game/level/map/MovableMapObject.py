from abc import ABC
from models.game.level.map.MapObject import MapObject
from models.game.level.map.MovableMapObjectDirection import (
    MapObjectDirection,
    MovableMapObjectDirections
)
from exceptions.map import *

class MovableMapObject(MapObject, ABC):
    def __init__(self,  position, direction=MovableMapObjectDirections.UP):
        super().__init__(position)
        if not isinstance(direction, MapObjectDirection):
            raise WrongDirectionDataException()
        self.__direction = direction

    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, direction):
        if not isinstance(direction, MapObjectDirection):
            raise WrongDirectionDataException()
        self.__direction = direction

    def move(self, position):
        self.position = position
    
    def __str__(self):
        return super().__str__()