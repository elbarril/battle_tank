class MapObjectPosition:
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
        if isinstance(other, MapObjectPosition):
            return self.x == other.x and self.y == other.y

    def __str__(self):
        return str(self.x) + str(self.y)
    
    def __radd__(self, other):
        if isinstance(other, MapObjectPosition):
            return MapObjectPosition(other.x + self.x, other.y + self.y)