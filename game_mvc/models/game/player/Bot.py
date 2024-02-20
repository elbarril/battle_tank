from models.game.player.AbstractPlayer import AbstractPlayer
from models.game.player.BotTank import BotTank
from constants.bot import *
from exceptions.bot import *

class Bot(AbstractPlayer):
    def __init__(self, tank:BotTank):
        self.tank = tank
        self.is_bot = True

    def add_tank(self, tank):
        if self.tank:
            raise BotAlreadyHasTankException()
        super().add_tank(tank)

    def __str__(self):
        return TO_STRING % self.number