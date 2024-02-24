from models.game.level.map.MovableMapObject import MovableMapObject
from constants.text import TO_STRING_TANK

class Tank(MovableMapObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_solid = True
        self.symbol = "T"

    def __str__(self):
        return super().__str__() % (TO_STRING_TANK, self.position)