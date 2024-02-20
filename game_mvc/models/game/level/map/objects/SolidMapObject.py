from models.game.level.map.MapObject import MapObject
    
class SolidMapObject(MapObject):
    symbol = "+"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_solid = True