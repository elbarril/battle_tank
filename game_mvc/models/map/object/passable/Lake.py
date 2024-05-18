from ..MapObjectSize import MapObjectSize
from ..abstract.PassableMapObjectCompound import PassableMapObjectCompound
from ..abstract.PassableMapObject import PassableMapObject


class Puddle(PassableMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.image = 'puddle'
        self.layer = 0

    def __str__(self):
        return "Puddle p:%s s:%s" % (self.position, self.size)


class Lake(PassableMapObjectCompound):
    def __init__(self, position, size):
        super().__init__(position, size, Puddle, MapObjectSize(2, 2))

    def __str__(self):
        return "Lake p:%s s:%s" % (self.position, self.size)
