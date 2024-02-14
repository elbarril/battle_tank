from model.MovableSingleMapObject import MovableSingleMapObject, Position
from model.Bullet import Bullet, BULLET_SIDE
from constants import (
    PIXELS,
    DIR_UP
)
TANK_SIDE = 4

class Tank(MovableSingleMapObject):
    def __init__(self, position:Position):
        super().__init__(position, TANK_SIDE, DIR_UP)

    def shoot(self) -> Bullet:
        move_y, move_x = self.direction
        y = self.position.y + move_y*self.radio/PIXELS + self.radio - BULLET_SIDE/2
        x = self.position.x + move_x*self.radio/PIXELS + self.radio - BULLET_SIDE/2
        return Bullet(Position(x, y), self.direction)