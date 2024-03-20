from models.map.MapObject import MapObject
from models.map.MapPosition import MapPosition
from models.map.MapObjectSize import MapObjectSize

from models.map.objects.FluidMapObject import FluidMapObject

from constants.map import MAP_WIDTH, MAP_HEIGHT

class Map:
    def __init__(self):
        self.__map = [[FluidMapObject(MapPosition(x,y), MapObjectSize(1,1)) for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]

    def is_valid_position(self, position):
        if not isinstance(position, MapPosition) and not isinstance(position, list):
            raise TypeError(f"Wrong position type: {position}")
        if isinstance(position, list):
            for pos in position:
                if not self.is_valid_position(pos):
                    return False
            return True
        else:
            return position.x >= 0 and position.y >= 0 and position.y < MAP_HEIGHT and position.x < MAP_WIDTH
    
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

    def __getitem__(self, position) -> MapObject:
        if not isinstance(position, MapPosition) and not isinstance(position, list):
            raise TypeError(f"Wrong position type: {position}")
        if isinstance(position, list):
            return [self[pos] for pos in position]
        x,y = position
        return self.__map[y][x]
        
    def __str__(self):
        objects = "\n".join([f"{str(map_object)}" for row in iter(self) for map_object in row])
        return f"Map (objects={objects})"