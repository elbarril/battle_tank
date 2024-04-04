from models.map.MapObject import MapObject
from models.map.MapPosition import MapPosition
from models.map.MovableObjectDirection import MovableObjectDirections
from constants import MAP_WIDTH_POSITIONS, MAP_HEIGHT_POSITIONS

class Map:
    def __init__(self, width=MAP_WIDTH_POSITIONS, height=MAP_HEIGHT_POSITIONS):
        self.__width = width
        self.__height = height
        self.__map = [[None for _ in range(MAP_WIDTH_POSITIONS)] for _ in range(MAP_HEIGHT_POSITIONS)]
        self.__objects = {None: MAP_HEIGHT_POSITIONS*MAP_WIDTH_POSITIONS}
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    def __iter__(self):
        return iter(self.__map)

    def __setitem__(self, position, map_object):
        if not isinstance(position, MapPosition) and not isinstance(position, list):
            raise TypeError(f"Wrong position type: {position}")
        if not isinstance(map_object, MapObject):
            raise TypeError(f"Wrong object type: {map_object}")
        if isinstance(position, list):
            for pos in position:
                self[pos] = map_object
        else:
            x,y = position
            self.__map[y][x] = map_object
            self.__save_object(map_object)

    def __save_object(self, map_object):
        object_type = repr(map_object)
        amount = self.__objects.get(object_type) + 1 if self.__objects.get(object_type) else 1
        self.__objects.update({object_type: amount})

    def __remove_object(self, map_object):
        object_type = repr(map_object) if map_object else None
        amount = self.__objects.get(object_type) - 1 if self.__objects.get(object_type) else 0
        self.__objects.update({object_type: amount})

    def __getitem__(self, position) -> MapObject:
        if not isinstance(position, MapPosition) and not isinstance(position, list):
            raise TypeError(f"Wrong position type: {position}")
        if isinstance(position, list):
            return [self[pos] for pos in position]
        x,y = position
        return self.__map[y][x]
    
    def __delitem__(self, position):
        if not isinstance(position, MapPosition) and not isinstance(position, list):
            raise TypeError(f"Wrong position type: {position}")
        if isinstance(position, list):
            for pos in position:
                del self[pos]
        else:
            x,y = position
            map_object = self.__map[y][x]
            self.__map[y][x] = None
            self.__remove_object(map_object)
        
    def __str__(self):
        return "\n"+"\n".join([f"\t- {type}: {amount}" for type,amount in self.__objects.items()])