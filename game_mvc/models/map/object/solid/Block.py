from ..MapObjectSize import MapObjectSize
from ..abstract.SolidMapObject import SolidMapObject
from ..abstract.SolidMapObjectCompound import SolidMapObjectCompound

class Iron(SolidMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.image = 'iron'

    def __str__(self):
        return "Iron p:%s s:%s" % (self.position, self.size)

class Block(SolidMapObjectCompound):
    def __init__(self, position, size):
        super().__init__(position, size, Iron, MapObjectSize(2,2))

    def __str__(self):
        return super().__str__() % ("Iron Compound", self.position, self.size)