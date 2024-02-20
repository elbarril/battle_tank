from models.game.player.AbstractPlayer import AbstractPlayer
from models.game.player.PlayerTank import PlayerTank
from constants.player import *
from exceptions.player import *

class Player(AbstractPlayer):
    char = None

    def add_tank(self, tank:PlayerTank):
        if self.tank:
            raise PlayerAlreadyHasTankException()
        super().add_tank(tank)

    def __str__(self):
        return TO_STRING % self.number