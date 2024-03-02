from models.map.MapObjectSize import MapObjectSize

class MapPosition:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    def __iter__(self):
        return iter((self.__x, self.__y))

    def __eq__(self, other):
        if isinstance(other, MapPosition):
            return self.x == other.x and self.y == other.y

    def __str__(self):
        return str(self.x) + str(self.y)
    
    def __add__(self, other):
        if isinstance(other, MapPosition):
            return MapPosition(int(other.x + self.x), int(other.y + self.y))
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        if isinstance(other, MapObjectSize):
            positions = []
            for y in range(other.height):
                for x in range(other.width):
                    positions.append(MapPosition(self.x + x, self.y + y))
            return positions

    def __rmul__(self, other):
        return self.__mul__(other)