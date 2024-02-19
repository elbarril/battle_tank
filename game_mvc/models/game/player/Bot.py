from models.game.player.AbstractPlayer import AbstractPlayer
from models.game.player.Tank import Tank
from constants.bot import *
from exceptions.bot import *

class Bot(AbstractPlayer):
    def __init__(self, tank:Tank):
        self.tank = tank
        self.is_bot = True

    def add_tank(self, tank):
        if self.tank:
            raise BotPlayerAlreadyHasTankException()
        self.tank = tank

    def __str__(self):
        return TO_STRING % self.number