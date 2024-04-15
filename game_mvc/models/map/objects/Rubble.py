from models.map.objects.PassableMapObject import PassableMapObject
    
class Rubble(PassableMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.image = 'rubble'
        self.layer = 0

    def __str__(self):
        return "Rubble p:%s s:%s" % (self.position, self.size)