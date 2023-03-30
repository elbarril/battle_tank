from model.game.Entity import Entity
from model.game.board.Position import Position

class Static(Entity):
    def __init__(self, position:Position, is_solid:bool):
        super().__init__(position=position, is_solid=is_solid)     

    def __repr__(self):
        return super().__repr__()
    