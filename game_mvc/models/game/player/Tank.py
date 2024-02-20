from models.game.level.map.MovableMapObject import MovableMapObject
from constants.tank import *

class Tank(MovableMapObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_solid = True
        self.symbol = "T"

    def __str__(self):
        return TO_STRING % self.position