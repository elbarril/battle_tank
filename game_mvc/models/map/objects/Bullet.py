from models.map.MovableMapObject import MovableMapObject
from models.map.objects.SolidMapObject import SolidMapObject

class Bullet(MovableMapObject, SolidMapObject):
    def __init__(self, position, size, direction):
        super().__init__(position, size, direction)
        self.symbol = "G"
        self.image = 'bullet'

    def __str__(self):
        return super().__str__() % ("Bullet", self.position, self.size)