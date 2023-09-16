from Player import Player
from Constants import SHOOT_KEYS, PLAYER1_DIRECTIONS

class Bot(Player):
    def __init__(self, row:int, column:int):
        super().__init__(row, column, PLAYER1_DIRECTIONS, SHOOT_KEYS)