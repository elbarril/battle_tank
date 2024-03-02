from models.map.MapSize import MapSize
from models.map.MapObject import MapObject
from models.map.MapObjectType import MapObjectType
from models.map.MapObjectPosition import MapObjectPosition
from models.map.MapMatrix import MapMatrix

from models.factories.MapObjectFactory import MapObjectFactory

class Map(MapMatrix):
    def __init__(self, map_size:MapSize=MapSize()):
        super().__init__(map_size)
        self.__size = map_size
    
    @property
    def width(self):
        return self.__size.width
    
    @property
    def height(self):
        return self.__size.height

    def is_valid_position(self, position:MapObjectPosition):
        for map_position in position:
            if map_position.x < 0 or map_position.y < 0 or map_position.y >= self.__size.height or map_position.x >= self.__size.width:
                return False
        return True
    
    def collision(self, object:MapObject, position:MapObjectPosition):
        for map_position in position:
            if object != self[map_position] and self[map_position].is_solid:
                return True
        return False
    
    def remove_object(self, object:MapObject):
        map_position = object.position[0]
        empty_object = MapObjectFactory.create(MapObjectType.FLUID, map_position.x, map_position.y)
        for map_position in object.position:
            self[map_position] = empty_object

    def add_object(self, object:MapObject):
        for map_position in object.position:
            self[map_position] = object