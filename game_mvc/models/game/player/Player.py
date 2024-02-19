from models.game.player.AbstractPlayer import AbstractPlayer
from models.game.player.Tank import Tank
from constants.player import *
from exceptions.player import *

class Player(AbstractPlayer):
    def add_tank(self, tank:Tank):
        if self.tank:
            raise PlayerAlreadyHasTankException()
        self.tank = tank
        self.tank.symbol = str(self.number)

    def __str__(self):
        return TO_STRING % self.number