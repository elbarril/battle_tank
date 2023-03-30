from model.game.entity.Static import Static
from model.game.board.Position import Position

class Water(Static):
    def __init__(self, position:Position):
        super().__init__(position=position, is_solid=False)

    def __str__(self):
        return "~"
    
    def __repr__(self):
        return "Water" + super().__repr__()