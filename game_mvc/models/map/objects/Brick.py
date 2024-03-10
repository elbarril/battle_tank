from models.map.objects.SolidMapObject import SolidMapObject
    
class Brick(SolidMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.image = 'brick'

    def __str__(self):
        return super().__str__() % ("Brick", self.position, self.size)