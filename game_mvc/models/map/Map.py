from models.map.MapObject import MapObject
from models.map.MapPosition import MapPosition
from models.map.MapObjectSize import MapObjectSize

from models.map.objects.FluidMapObject import FluidMapObject

from constants.map import MAP_WIDTH, MAP_HEIGHT, MAP_COLUMNS, MAP_ROWS

class Map:
    def __init__(self, width=MAP_WIDTH, height=MAP_HEIGHT):
        self.__width = width
        self.__height = height
        self.__map = [[FluidMapObject(MapPosition(x,y), MapObjectSize(1,1)) for x in range(width)] for y in range(height)]
        self.__objects = {}
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height

    def is_valid_position(self, position):
        if not isinstance(position, MapPosition) and not isinstance(position, list):
            raise TypeError(f"Wrong position type: {position}")
        if isinstance(position, list):
            for pos in position:
                if not self.is_valid_position(pos):
                    return False
            return True
        else:
            return position.x >= 0 and position.y >= 0 and position.y < MAP_ROWS and position.x < MAP_COLUMNS
    
    def __iter__(self):
        return iter(self.__map)

    def __setitem__(self, position, map_object):
        if not isinstance(position, MapPosition) and not isinstance(position, list):
            raise TypeError(f"Wrong position type: {position}")
        if not isinstance(map_object, MapObject):
            raise TypeError(f"Object is not MapObject type: {map_object}")
        if isinstance(position, list):
            for pos in position:
                self[pos] = map_object
        else:
            x,y = position
            self.__map[y][x] = map_object
            object_type = type(map_object)
            amount = self.__objects.get(object_type) + 1 if self.__objects.get(object_type) else 0
            self.__objects.update({object_type: amount})

    def __getitem__(self, position) -> MapObject:
        if not isinstance(position, MapPosition) and not isinstance(position, list):
            raise TypeError(f"Wrong position type: {position}")
        if isinstance(position, list):
            return [self[pos] for pos in position]
        x,y = position
        return self.__map[y][x]
        
    def __str__(self):
        objects = "\n".join([f"{type}: {amount}" for type,amount in self.__objects.items()])
        return f"Map (objects={objects})"