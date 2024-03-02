from models.map.objects.SolidMapObjectCompound import SolidMapObjectCompound
from models.map.objects.Brick import Brick
    
class BrickCompound(SolidMapObjectCompound):
    def __init__(self, position,):
        super().__init__(position, Brick)