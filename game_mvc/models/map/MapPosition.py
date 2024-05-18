from .object.MapObjectSize import MapObjectSize


class MapPositionCollection:
    def __init__(self, positions=None):
        self.__positions = []
        if positions:
            if not isinstance(positions, list):
                raise TypeError("Wrong positions type")
            for position in positions:
                self.add(position)

    def add(self, position):
        if not isinstance(position, MapPosition):
            raise TypeError("Wrong position type")
        self.__positions.append(position)

    def __iter__(self):
        return iter(self.__positions)


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

    def __add__(self, other):
        if isinstance(other, (MapPosition, MapObjectSize)):
            x, y = other
            return MapPosition(int(x + self.x), int(y + self.y))

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, (MapPosition, MapObjectSize)):
            positions = MapPositionCollection()
            x_pos, y_pos = other
            for y in range(y_pos):
                for x in range(x_pos):
                    positions.add(MapPosition(self.x + x, self.y + y))
            return positions

    def __rmul__(self, other):
        return self.__mul__(other)

    def __floordiv__(self, other):
        if isinstance(other, int):
            return MapPosition(self.x // other, self.y // other)

    def __str__(self):
        return "x:%d y:%d" % (self.x, self.y)
