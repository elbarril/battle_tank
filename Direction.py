from Keyboard import *
from Position import Position

DIRECTIONS = {
    UP_DIRECTION_KEY: (-1,0),
    DOWN_DIRECTION_KEY: (1,0),
    LEFT_DIRECTION_KEY: (0,-1),
    RIGHT_DIRECTION_KEY: (0,1)
}

class Direction(Position):
    def __init__(self, key:str=UP_DIRECTION_KEY):
        if DIRECTIONS.get(key) is None:
            raise Exception()
        row, column = DIRECTIONS[key]
        super().__init__(row, column)