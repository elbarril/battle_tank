from models.map.MovableMapObject import MovableMapObject
from models.map.objects.SolidMapObject import SolidMapObject
from models.map.objects.Bullet import Bullet

from constants.text import TO_STRING_TANK

class Tank(MovableMapObject, SolidMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.symbol = "T"

    def shoot(self):
        next_position = self.position + self.direction
        return Bullet(next_position[0], self.direction)

    def __str__(self):
        return super().__str__() % (TO_STRING_TANK, self.position, self.size)