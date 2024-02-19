from models.game.level.map.MovableMapObject import MovableMapObject
from constants.tank import *

class Tank(MovableMapObject):
    symbol = "T"

    def __init__(self, player, position):
        super().__init__(position)
        self.player = player
        self.is_solid = True
        self.symbol = "B" if self.player.is_bot else str(self.player.number)

    @property
    def x(self): return self.position.x

    @property
    def y(self): return self.position.y

    def __str__(self):
        return TO_STRING % (self.player, self.position)