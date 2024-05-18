from .Tank import Tank
from ..MapObjectSize import MapObjectSize
from .. import MapObjectDirection as directions
from ..abstract.SolidMapObject import SolidMapObject
from ..abstract.MovableMapObject import MovableMapObject


class Bullet(MovableMapObject, SolidMapObject):
    def __init__(self, tank: Tank):
        self.tank = tank
        position = tank.position + tank.direction
        size = None
        w, h = tank.size
        if tank.direction in (directions.UP, directions.DOWN):
            size = MapObjectSize(2, 1)
            if tank.direction is directions.UP:
                position += MapObjectSize((w-size.width)//2, 0)
            elif tank.direction is directions.DOWN:
                position += MapObjectSize((w-size.width)//2, h-size.height)
        else:
            size = MapObjectSize(1, 2)
            if tank.direction is directions.RIGHT:
                position += MapObjectSize(w-size.width,  (h-size.height)//2)
            elif tank.direction is directions.LEFT:
                position += MapObjectSize(0, (h-size.height)//2)
        super().__init__(position, size, tank.direction)
        self.symbol = "G"
        self.image = 'bullet'
