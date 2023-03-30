from model.game.entity.Static import Static
from model.game.board.Position import Position

class Brick(Static):
   def __init__(self, position:Position):
      super().__init__(position=position, is_solid=True)

   def __str__(self):
      return "◘"
    
   def __repr__(self):
      return "Birck" + super().__repr__()