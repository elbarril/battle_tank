from models.game.map.MapSize import MapSize
from models.game.map.MapObject import MapObject
from models.game.map.MapObjectType import MapObjectType
from models.game.map.MapObjectPosition import MapObjectPosition
from models.game.map.MapMatrix import MapMatrix

from models.game.factories.MapObjectFactory import MapObjectFactory

class Map(MapMatrix):
    def __init__(self, map_size:MapSize=MapSize()):
        super().__init__(map_size)
        self.__size = map_size

    def is_valid_position(self, position:MapObjectPosition):
        return position.x >=0 and position.y >= 0 and position.y < self.__size.height and position.x < self.__size.width
    
    def collision(self, position:MapObjectPosition):
        return self[position].is_solid
    
    def remove_object(self, object:MapObject):
        self[object.position] = MapObjectFactory.create(MapObjectType.FLUID, object.position.x, object.position.y)

    def add_object(self, object:MapObject):
        self[object.position] = object