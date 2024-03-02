from models.map.MapObject import MapObject
    
class SolidMapObject(MapObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = "+"
        self.is_solid = True
        self.color = 'red'