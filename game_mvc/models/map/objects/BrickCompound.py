from models.map.objects.SolidMapObjectCompound import SolidMapObjectCompound
from models.map.objects.Brick import Brick
    
class BrickCompound(SolidMapObjectCompound):
    def __init__(self, position, size):
        super().__init__(position, size, Brick)

    def __str__(self):
        return super().__str__() % ("Brick Compound", self.position, self.size)