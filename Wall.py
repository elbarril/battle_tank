WALL_WIDTH = WALL_HEIGHT = 3
MAP_OBJECT_RADIO = WALL_WIDTH//2
from Brick import Brick

class Wall:
    def __init__(self, row:int, column:int):
        self.__bricks = [Brick(row+y,column+x) for x in range(WALL_WIDTH) for y in range(WALL_HEIGHT)]
        
    @property
    def bricks(self) -> list[Brick]:
        return self.__bricks