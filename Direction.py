from Keyboard import *

DIRECTIONS = {
    UP_DIRECTION_KEY: (-1,0),
    DOWN_DIRECTION_KEY: (1,0),
    LEFT_DIRECTION_KEY: (0,-1),
    RIGHT_DIRECTION_KEY: (0,1)
}

class Direction:
    def __init__(self, key:str=UP_DIRECTION_KEY):
        if DIRECTIONS.get(key) is None:
            raise Exception()
        self.__row, self.__column = DIRECTIONS.get(key)
    
    @property
    def row(self) -> int:
        return self.__row
    
    @property
    def column(self) -> int:
        return self.__column

    def __str__(self):
        return f"{self.row, self.column}"