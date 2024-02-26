from models.game.map.MapObject import MapObject

class FluidMapObject(MapObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_solid = False
        self.symbol = ' '