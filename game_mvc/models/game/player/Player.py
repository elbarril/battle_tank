from models.game.player.Tank import Tank
from constants.player import *
from exceptions.player import *

class Player:
    tank = None
    number = ''
    is_bot = None
    movements = None

    def create_tank(self, position):
        if self.tank:
            raise PlayerAlreadyHasTankException()
        self.tank = Tank(self, position)
        return self.tank

    def __str__(self):
        return TO_STRING % self.number