from abc import ABC
from models.game.level.map.MapObjectPosition import MapObjectPosition
from models.game.level.map.MapObjectSize import MapObjectSize

class MapObject(ABC):
    is_solid = None
    symbol = None

    def __init__(self, position:MapObjectPosition, size=MapObjectSize(1,1)):
        self.position = position
        self.size = size
    
    def __str__(self):
        return self.symbol
    