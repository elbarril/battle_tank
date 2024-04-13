from models.map.MovableMapObject import MovableMapObject
from models.map.objects.SolidMapObject import SolidMapObject
from models.map.objects.Bullet import Bullet
from models.map.MapObjectSize import MapObjectSize
from models.map.MapObjectDirection import *

class Tank(MovableMapObject, SolidMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.symbol = "T"

    def shoot(self):
        next_position = self.position + self.direction
        size = None
        if self.direction in (UP,DOWN):
            size = MapObjectSize(2,1)
        else:
            size = MapObjectSize(1,2)
        if self.direction is RIGHT:
            x,y = self.size
            next_position += MapObjectSize(x//x, 0)
        elif self.direction is DOWN:
            x,y = self.size
            next_position += MapObjectSize(0, y//y)
        return Bullet(next_position, size, self.direction)