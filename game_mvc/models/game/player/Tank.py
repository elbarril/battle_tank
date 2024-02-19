from models.game.level.map.MovableMapObject import MovableMapObject
from constants.tank import *

class Tank(MovableMapObject):

    def __init__(self, position):
        super().__init__(position)
        self.is_solid = True
        self.symbol = "T"

    @property
    def x(self): return self.position.x

    @property
    def y(self): return self.position.y

    def __str__(self):
        return TO_STRING % self.position