from models.game.player.Player import Player
from constants.bot import *
from exceptions.bot import *

class Bot(Player):
    is_bot = True

    def create_tank(self, position):
        if self.tank:
            raise BotPlayerAlreadyHasTankException()
        return super().create_tank(position)

    def __str__(self):
        return TO_STRING % self.number