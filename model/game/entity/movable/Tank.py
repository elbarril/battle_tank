from model.game.entity.Movable import Movable
from model.game.entity.movable.Bullet import Bullet
from model.game.board.Position import Position

class Tank(Movable):
    def __init__(self, position:Position, direction:str, speed:int):
        super().__init__(position=position, direction=direction, speed=speed)

    def shoot(self) -> Bullet:
        return Bullet(self.position, self.direction)
        
    def __str__(self):
        return "☻"

    def __repr__(self):
        return "Tank" + super().__repr__()