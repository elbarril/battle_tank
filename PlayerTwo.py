from Player import Player
from Constants import (
    PLAYER2_DIRECTIONS,
    PLAYER2_SHOOT_KEYS
)

class PlayerTwo(Player):
    def __init__(self, row, column):
        super().__init__(row, column, PLAYER2_DIRECTIONS, PLAYER2_SHOOT_KEYS)