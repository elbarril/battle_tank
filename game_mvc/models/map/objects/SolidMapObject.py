from models.map.MapObject import MapObject
    
class SolidMapObject(MapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.symbol = "+"
        self.is_solid = True
        self.color = 'red'