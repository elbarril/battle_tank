from models.game.player.AbstractPlayer import AbstractPlayer
from models.game.player.PlayerTank import PlayerTank

from constants.text import TO_STRING_PLAYER

class Player(AbstractPlayer):
    def __init__(self, number):
        super().__init__(number)

    def add_tank(self, tank:PlayerTank):
        super().add_tank(tank)

    def __str__(self):
        return TO_STRING_PLAYER % self.number