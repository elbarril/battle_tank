from models.map.objects.PassableMapObjectCompound import PassableMapObjectCompound
from models.map.objects.Rubble import Rubble
from models.map.MapObjectSize import MapObjectSize

class Gravel(PassableMapObjectCompound):
    def __init__(self, position, size):
        super().__init__(position, size, Rubble, MapObjectSize(2,2))

    def __str__(self):
        return "Gravel p:%s s:%s" % (self.position, self.size)