from models.map.objects.SolidMapObject import SolidMapObject
    
class Brick(SolidMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.image = 'brick'