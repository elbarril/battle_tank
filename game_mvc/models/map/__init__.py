from models.map.MapObject import MapObject
from models.map.MapPosition import MapPosition, MapPositionCollection

class Map:
    def __init__(self):
        self.__background_color = 'black'
        self.__width = 13 * 4
        self.__height = 13 * 4
        self.__map = [[None for _ in range(self.__width)] for _ in range(self.__height)]
        self.__layers = []
    
    @property
    def background_color(self):
        return self.__background_color

    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @property
    def layers(self):
        return self.__layers
    
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
            if map_object.layer not in self.__layers: self.__layers.append(map_object.layer)

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
            self.__map[y][x] = None

    def __contains__(self, position):
        if not isinstance(position, (MapPosition, MapPositionCollection)):
            raise TypeError(f"Wrong position type: {position}")
        if isinstance(position, MapPositionCollection):
            for pos in position:
                if pos in self: continue
                else: return False
            return True
        else: return -1 < position.y < self.__width and -1 < position.x < self.__width
