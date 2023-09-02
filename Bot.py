from Player import Player

class Bot(Player):
    def __init__(self, row:int, column:int):
        super().__init__(row, column)
        self.tank.can_be_destroyed = True