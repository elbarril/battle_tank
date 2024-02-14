from model.MultipleMapObject import MultipleMapObject
from model.Position import Position
WALL_SIDE = 4
BRICK_SIZE = 2

class Wall(MultipleMapObject):
    def __init__(self, map_positions:Position):
        super().__init__(map_positions, WALL_SIDE, BRICK_SIZE)
