from abc import ABC
from models.game.level.map.MapObject import MapObject
from models.game.level.map.MovableMapObjectDirection import (
    MapObjectDirection,
    MovableMapObjectDirections
)

class MovableMapObject(MapObject, ABC):
    def __init__(self,  position, direction=MovableMapObjectDirections.UP):
        super().__init__(position)
        self.__direction = direction

    @property
    def direction(self) -> MapObjectDirection:
        return self.__direction
    
    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    def move(self, position):
        self.position = position
    
    def __str__(self):
        return super().__str__()