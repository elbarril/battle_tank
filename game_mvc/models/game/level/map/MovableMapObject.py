from models.game.level.map.MapObject import MapObject
from models.game.level.map.MovableMapObjectDirection import MapObjectDirection
from exceptions.map import *

class MovableMapObject(MapObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def move(self, direction):
        if not isinstance(direction, MapObjectDirection):
            raise WrongDirectionDataException()
        self.position = self.next_position(direction)

    def next_position(self, direction):
        if not isinstance(direction, MapObjectDirection):
            raise WrongDirectionDataException()
        return self.position + direction
    