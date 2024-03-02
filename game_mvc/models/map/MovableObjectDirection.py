from models.map.MapPosition import MapPosition

class MovableObjectDirection(MapPosition):
    def __init__(self, x, y, string):
        super().__init__(x, y)
        self.__string = string

    def __str__(self):
        return self.__string

class MovableObjectDirections:
    UP = MovableObjectDirection(0, -1, 'up')
    DOWN = MovableObjectDirection(0, 1, 'down')
    LEFT = MovableObjectDirection(-1, 0, 'left')
    RIGHT = MovableObjectDirection(1, 0, 'right')