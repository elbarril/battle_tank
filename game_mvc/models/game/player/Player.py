from models.game.player.AbstractPlayer import AbstractPlayer
from models.game.player.PlayerTank import PlayerTank

from constants.text import TO_STRING_PLAYER 
from exceptions.player import *

class Player(AbstractPlayer):
    type = None

    def add_tank(self, tank:PlayerTank):
        if self.tank:
            raise PlayerAlreadyHasTankException()
        super().add_tank(tank)

    def __str__(self):
        return TO_STRING_PLAYER % self.number