from models.map.MapPosition import MapPosition


class MapObjectDirection(MapPosition):
    def __init__(self, x, y, string):
        super().__init__(x, y)
        self.__string = string

    @property
    def string(self):
        return self.__string


UP = MapObjectDirection(0, -1, 'up')
DOWN = MapObjectDirection(0, 1, 'down')
LEFT = MapObjectDirection(-1, 0, 'left')
RIGHT = MapObjectDirection(1, 0, 'right')
