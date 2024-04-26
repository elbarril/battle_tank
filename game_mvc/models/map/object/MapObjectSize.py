class MapObjectSize:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
    
    def __iter__(self):
        return iter((self.width, self.height))

    def __truediv__(self, other):
        if isinstance(other, int):
            result = self.__floordiv__(other)
            return result
        
    def __floordiv__(self, other):
        if isinstance(other, (MapObjectSize,int)):
            if isinstance(other, int):
                return MapObjectSize(self.width // 2, self.height // 2)
            else:
                return MapObjectSize(self.width // other.width, self.height // other.height)
    
    def __str__(self):
        return "w:%d h:%d" % (self.width, self.height)