from models.map.MapSize import MapSize
from models.map.MapObject import MapObject
from models.map.MapObjectCompound import MapObjectCompound
from models.map.MapObjectPosition import MapObjectPosition

from models.factories.MapObjectFactory import MapObjectFactory
from constants.map import MAP_WIDTH, MAP_HEIGHT, MAP_POSITION_WIDTH, MAP_POSITION_HEIGHT

class Map:
    def __init__(self, map_size:MapSize=None):
        if map_size and not isinstance(map_size, MapSize):
            raise TypeError(f"Object is not MapSize type: {map_size}")
        self.__size = map_size or MapSize(MAP_WIDTH*MAP_POSITION_WIDTH, MAP_HEIGHT*MAP_POSITION_HEIGHT)
        self.__matrix = [[MapObjectFactory.create_empty(x, y, None) for x in range(self.__size.width)] for y in range(self.__size.height)]

    @property
    def size(self):
        return self.__size

    def is_valid_position(self, object_position):
        if not isinstance(object_position, MapObjectPosition):
            raise TypeError(f"Object is not MapObjectPosition type: {object_position}")
        for map_position in object_position:
            if map_position.x < 0 or map_position.y < 0 or map_position.y >= self.__size.height or map_position.x >= self.__size.width:
                return False
        return True
    
    def __iter__(self):
        return iter(self.__matrix)

    def __setitem__(self, object_position, map_object):
        if not isinstance(object_position, MapObjectPosition):
            raise TypeError(f"Object is not MapObjectPosition type: {object_position}")
        if not isinstance(map_object, MapObject):
            raise TypeError(f"Object is not MapObject type: {map_object}")
        if isinstance(map_object, MapObjectCompound):
            for object in map_object:
                self[object.position] = object
        else:
            for map_position in object_position:
                self.__matrix[map_position.y][map_position.x] = map_object

    def __getitem__(self, object_position) -> MapObject | None:
        if not isinstance(object_position, MapObjectPosition):
            raise TypeError(f"Object is not MapObjectPosition type: {object_position}")
        return [self.__matrix[map_position.y][map_position.x] for map_position in object_position]
    
    def __delitem__(self, map_object):
        if not isinstance(map_object, MapObject):
            raise TypeError(f"Object is not MapObject type: {map_object}")
        empty_object = MapObjectFactory.create_empty(map_object.position[0].x, map_object.position[0].y, map_object.size)
        self[map_object.position] = empty_object
        
    def __str__(self):
        objects = "\n".join([f"{str(map_object)}" for row in iter(self) for map_object in row])
        return f"Map (objects={objects})"