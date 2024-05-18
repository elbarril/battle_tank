from ..abstract.PassableMapObjectCompound import PassableMapObjectCompound
from ..abstract.PassableMapObject import PassableMapObject
from ..MapObjectSize import MapObjectSize


class Rubble(PassableMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.image = 'rubble'
        self.layer = 0

    def __str__(self):
        return "Rubble p:%s s:%s" % (self.position, self.size)


class Gravel(PassableMapObjectCompound):
    def __init__(self, position, size):
        super().__init__(position, size, Rubble, MapObjectSize(2, 2))

    def __str__(self):
        return "Gravel p:%s s:%s" % (self.position, self.size)
