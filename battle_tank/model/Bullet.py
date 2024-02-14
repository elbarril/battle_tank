from model.MovableSingleMapObject import MovableSingleMapObject, Position
BULLET_SIDE = 1
class Bullet(MovableSingleMapObject):
    def __init__(self, position:Position, direction:str):
        super().__init__(position, BULLET_SIDE, direction)