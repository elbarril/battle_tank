from models.map.objects.SolidMapObjectCompound import SolidMapObjectCompound
from models.map.objects.Iron import Iron
from models.map.MapObjectSize import MapObjectSize
    
class Block(SolidMapObjectCompound):
    def __init__(self, position, size):
        super().__init__(position, size, Iron, MapObjectSize(2,2))

    def __str__(self):
        return super().__str__() % ("Iron Compound", self.position, self.size)