from ..MapObjectSize import MapObjectSize
from ..abstract.PassableMapObject import PassableMapObject
from ..abstract.PassableMapObjectCompound import PassableMapObjectCompound


class Tree(PassableMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.image = 'tree'
        self.layer = 2

    def __str__(self):
        return "Tree p:%s s:%s" % (self.position, self.size)


class Forest(PassableMapObjectCompound):
    def __init__(self, position, size):
        super().__init__(position, size, Tree, MapObjectSize(2, 2))
