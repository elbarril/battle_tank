from model.game.entity.static.Brick import Brick
from model.game.entity.static.Path import Path
from model.game.entity.static.Stone import Stone
from model.game.entity.static.Water import Water
from model.game.entity.static.Metal import Metal
from model.game.entity.static.Earth import Earth
from model.game.entity.static.Bush import Bush

from enum import Enum

class STATIC_CLASSES(Enum):
    B = Brick
    P = Path
    S = Stone
    W = Water
    M = Metal
    E = Earth
    F = Bush