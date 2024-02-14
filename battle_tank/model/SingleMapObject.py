from model.MapObject import MapObject, Position

class SingleMapObject(MapObject):
    def __init__(self, position:Position, side:int):
        super().__init__(position, side)

    @property
    def list(self): return super().list