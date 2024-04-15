from models.map.objects.SolidMapObject import SolidMapObject
    
class Iron(SolidMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.image = 'iron'

    def __str__(self):
        return "Iron p:%s s:%s" % (self.position, self.size)