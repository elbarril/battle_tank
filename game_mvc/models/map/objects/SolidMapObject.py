from models.map.MapObject import MapObject
    
class SolidMapObject(MapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.symbol = "+"
        self.color = 'red'

    def __str__(self):
        return super().__str__()