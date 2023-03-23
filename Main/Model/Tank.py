from Main.Model.Bullet import Bullet
from Main.Model.Movable import Movable
from typing import Literal

class Tank(Movable):
    def __init__(self, column:int, row:int, direction:Literal["up", "down", "left", "right"], speed:int):
        super().__init__(column=column, row=row, direction=direction, speed=speed)

    def shoot(self) -> Bullet:
        return Bullet(self.column, self.row, self.direction)
        
    def __str__(self):
        return "☻"
