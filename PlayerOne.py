from Player import Player
from Constants import (
    PLAYER1_DIRECTIONS,
    PLAYER1_SHOOT_KEYS
)

class PlayerOne(Player):
    def __init__(self, row, column):
        super().__init__(row, column, PLAYER1_DIRECTIONS, PLAYER1_SHOOT_KEYS)