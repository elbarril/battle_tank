class MapObjectSize:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __truediv__(self, other):
        if isinstance(other, int):
            result = self.__floordiv__(other)
            return result
        
    def __floordiv__(self, other):
        if isinstance(other, int):
            return MapObjectSize(self.width // (other // 2), self.height // (other // 2))
    
    def __str__(self):
        return str(self.width) + str(self.height)