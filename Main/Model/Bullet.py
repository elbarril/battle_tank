from Main.Model.Movable import Movable
from typing import Literal
class Bullet(Movable):
    def __init__(self, column:int, row:int, direction:Literal["up", "down", "left", "right"]):
        #bullet_row = (row - 1) if direction == "up" else (row + 1) if direction == "up" else row
        #bullet_column = (column - 1) if direction == "left" else (column + 1) if direction == "right" else column
        #super().__init__(column=bullet_column, row=bullet_row, direction=direction, speed=1)
        super().__init__(column=column, row=row, direction=direction, speed=1)
        
    def __str__(self):
        return "#"