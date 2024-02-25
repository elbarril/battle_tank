class MapObjectPosition:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, MapObjectPosition):
            return self.x == other.x and self.y == other.y

    def __str__(self):
        return str(self.x) + str(self.y)
    
    def __radd__(self, other):
        if isinstance(other, MapObjectPosition):
            return MapObjectPosition(other.x + self.x, other.y + self.y)