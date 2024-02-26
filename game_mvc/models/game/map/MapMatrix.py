from models.game.map.MapObject import MapObject
from models.game.map.MapObjectPosition import MapObjectPosition
from models.game.map.MapSize import MapSize

class MapMatrix:
    def __init__(self, size:MapSize):
        self.__matrix = [[None for _ in range(size.width)] for _ in range(size.height)]
    
    def __setitem__(self, position:MapObjectPosition, object:MapObject):
        self.__matrix[position.y][position.x] = object

    def __getitem__(self, position:MapObjectPosition) -> MapObject:
        return self.__matrix[position.y][position.x]
    
    def __iter__(self):
        return iter(self.__matrix)
    
    def __len__(self):
        return len(self.__matrix)