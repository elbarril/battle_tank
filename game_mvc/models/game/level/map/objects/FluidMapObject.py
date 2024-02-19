from models.game.level.map.MapObject import MapObject

class FluidMapObject(MapObject):
    symbol = "F"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_solid = False