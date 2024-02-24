from abc import ABC
from models.game.level.map.MapObjectPosition import MapObjectPosition
from models.game.level.map.MapObjectSize import MapObjectSize

class MapObject(ABC):
    is_solid = None
    symbol = None

    def __init__(self, position:MapObjectPosition, size=MapObjectSize(1,1)):
        self.position = position
        self.size = size
    
    @property
    def x(self): return self.position.x

    @property
    def y(self): return self.position.y

    def __str__(self):
        return f"{self.position}"
    