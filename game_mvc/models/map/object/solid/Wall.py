from ..MapObjectSize import MapObjectSize
from ..abstract.SolidMapObjectCompound import SolidMapObjectCompound
from ..abstract.SolidMapObject import SolidMapObject
    
class Brick(SolidMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.image = 'brick'

    def __str__(self):
        return "Brick p:%s s:%s" % (self.position, self.size)

class Wall(SolidMapObjectCompound):
    def __init__(self, position, size):
        super().__init__(position, size, Brick, MapObjectSize(1,1))

    def __str__(self):
        return super().__str__() % ("Brick Compound", self.position, self.size)