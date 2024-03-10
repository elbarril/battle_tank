from models.map.MovableMapObject import MovableMapObject
from models.map.MapObjectSize import MapObjectSize
from models.map.objects.SolidMapObject import SolidMapObject

class Bullet(MovableMapObject, SolidMapObject):
    def __init__(self, position, direction):
        super().__init__(position, MapObjectSize(1,1), direction)
        self.symbol = "G"
        self.image = 'bullet'

    def __str__(self):
        return super().__str__() % ("Bullet", self.position, self.size)