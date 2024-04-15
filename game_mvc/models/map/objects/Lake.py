from models.map.objects.PassableMapObjectCompound import PassableMapObjectCompound
from models.map.objects.Puddle import Puddle
from models.map.MapObjectSize import MapObjectSize

class Lake(PassableMapObjectCompound):
    def __init__(self, position, size):
        super().__init__(position, size, Puddle, MapObjectSize(2,2))

    def __str__(self):
        return "Lake p:%s s:%s" % (self.position, self.size)