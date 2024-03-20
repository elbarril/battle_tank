from models.map.MovableMapObject import MovableMapObject
from models.map.objects.SolidMapObject import SolidMapObject
from models.map.objects.Bullet import Bullet
from models.map.MapObjectSize import MapObjectSize
from models.map.MovableObjectDirection import MovableObjectDirections

from constants.text import TO_STRING_TANK

class Tank(MovableMapObject, SolidMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.symbol = "T"

    def shoot(self):
        next_position = self.position + self.direction
        size = None
        if self.direction in (MovableObjectDirections.UP,MovableObjectDirections.DOWN):
            size = MapObjectSize(2,1)
        else:
            size = MapObjectSize(1,2)
        if self.direction is MovableObjectDirections.RIGHT:
            x,y = self.size
            next_position += MapObjectSize(x//x, 0)
        elif self.direction is MovableObjectDirections.DOWN:
            x,y = self.size
            next_position += MapObjectSize(0, y//y)
        return Bullet(next_position, size, self.direction)

    def __str__(self):
        return super().__str__() % (TO_STRING_TANK, self.position, self.size)