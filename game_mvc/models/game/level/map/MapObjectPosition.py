from exceptions.position import *

class MapObjectPosition:
    def __init__(self, x, y):
        if not (isinstance(x, int) and isinstance(y, int)):
            raise WrongPositionValueTypeException()
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, MapObjectPosition):
            raise NotPositionTypeException()
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return str(self.x) + str(self.y)
    
    def __radd__(self, other):
        if not isinstance(other, MapObjectPosition):
            raise NotPositionTypeException()
        return MapObjectPosition(other.x + self.x, other.y + self.y)