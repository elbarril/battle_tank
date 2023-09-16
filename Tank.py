from MovableMapObject import MovableMapObject
from Bullet import Bullet
from Direction import Direction
from Constants import DIRECTION_UP

class Tank(MovableMapObject):
    def __init__(self, row:int, column:int, size:int, image_filename:str):
        super().__init__(row, column, size, image_filename, Direction(DIRECTION_UP))
        self.can_be_destroyed = True

    def shoot(self) -> Bullet:
        row = self.row + self.direction.row
        column = self.column + self.direction.column
        return Bullet(row, column, self.direction, self)