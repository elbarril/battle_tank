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
        if isinstance(other, int):
            return MapObjectSize(self.width // (other // 2), self.height // (other // 2))
    
    def __str__(self):
        return f"MapObjectSize(width={self.width}, height={self.height})"