from Player import Player
from Brick import Brick

LEVELS = {
    1: {
        "player": (25,25),
        "obstacles": [
            (5,5),
            (6,6),
            (5,6),
            (6,5)
        ]
    }
}

class Level:
    def __init__(self, key:int):
        self.__key = key
        
    @property
    def obstacles(self) -> list[Brick]:
        return [Brick(row, column) for (row, column) in LEVELS[self.__key]["obstacles"]]
    
    @property
    def player(self) -> Player:
        row, column = LEVELS[self.__key]["player"]
        return Player(row, column)
        
    