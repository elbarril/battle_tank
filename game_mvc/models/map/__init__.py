from models.map.MapObject import MapObject
from models.map.MapPosition import MapPosition, MapPositionCollection

class Map:
    def __init__(self):
        self.__width = 20
        self.__height = 20
        self.__map = [[None for _ in range(self.__width)] for _ in range(self.__height)]
        self.__objects = {None: self.__height*self.__width}
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    def __iter__(self):
        return iter(self.__map)

    def __setitem__(self, position, map_object):
        if not isinstance(position, (MapPosition, MapPositionCollection)):
            raise TypeError(f"Wrong position type: {position}")
        if not isinstance(map_object, MapObject):
            raise TypeError(f"Wrong object type: {map_object}")
        if isinstance(position, MapPositionCollection):
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
        if not isinstance(position, (MapPosition, MapPositionCollection)):
            raise TypeError(f"Wrong position type: {position}")
        if isinstance(position, MapPositionCollection):
            return [self[pos] for pos in position]
        x,y = position
        return self.__map[y][x]
    
    def __delitem__(self, position):
        if not isinstance(position, (MapPosition, MapPositionCollection)):
            raise TypeError(f"Wrong position type: {position}")
        if isinstance(position, MapPositionCollection):
            for pos in position:
                del self[pos]
        else:
            x,y = position
            map_object = self.__map[y][x]
            self.__map[y][x] = None
            self.__remove_object(map_object)

    def __contains__(self, position):
        if not isinstance(position, (MapPosition, MapPositionCollection)):
            raise TypeError(f"Wrong position type: {position}")
        if isinstance(position, MapPositionCollection):
            for pos in position:
                if pos in self: continue
                else: return False
            return True
        else: return -1 < position.y < self.__width and -1 < position.x < self.__width

    def __str__(self):
        return "\n"+"\n".join([f"\t- {type}: {amount}" for type,amount in self.__objects.items()])