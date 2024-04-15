from models.map.objects.PassableMapObject import PassableMapObject
    
class Tree(PassableMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.image = 'tree'
        self.layer = 2

    def __str__(self):
        return "Tree p:%s s:%s" % (self.position, self.size)