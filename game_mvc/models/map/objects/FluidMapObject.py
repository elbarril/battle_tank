from models.map.MapObject import MapObject

class FluidMapObject(MapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.symbol = ' '
        self.color = ''

    def __str__(self):
        return super().__str__() % ("Fluid", self.position, self.size)