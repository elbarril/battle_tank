from model.game.entity.Movable import Movable
from model.game.board.Position import Position

class Bullet(Movable):
    def __init__(self, position:Position, direction:str):
        super().__init__(position=position, direction=direction, speed=1)
        
    def __str__(self):
        return "#"
    
    def __repr__(self):
        return "Bullet" + super().__repr__()