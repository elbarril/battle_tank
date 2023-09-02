from Player import Player
from Brick import Brick
from Bot import Bot

LEVELS = {
    1: {
        "player": (25,25),
        "obstacles": [
            (1,25),(1,26),(1,27),(1,28),
            (2,25),(2,26),(2,27),(2,28)
        ],
        "bots": [
            (33,33),
            (33,10)
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
        
    @property
    def bots(self) -> list[Bot]:
        return [Bot(row, column) for (row, column) in LEVELS[self.__key]["bots"]]