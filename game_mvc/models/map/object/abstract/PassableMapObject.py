from .. import MapObject


class PassableMapObject(MapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.symbol = "'"
        self.color = 'green'

    def __str__(self):
        return super().__str__()
