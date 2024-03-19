from models.map.objects.SolidMapObjectCompound import SolidMapObjectCompound
from models.map.objects.Brick import Brick
from models.map.MapObjectSize import MapObjectSize
    
class BrickCompound(SolidMapObjectCompound):
    def __init__(self, position, size):
        super().__init__(position, size, Brick,  MapObjectSize(1,1))

    def __str__(self):
        return super().__str__() % ("Brick Compound", self.position, self.size)