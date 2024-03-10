from models.player.AbstractPlayer import AbstractPlayer

from constants.text import TO_STRING_BOT

class Bot(AbstractPlayer):
    number = 0
    def __init__(self, tank):
        Bot.number += 1
        super().__init__(Bot.number, tank)
        self.is_bot = True

    def add_tank(self, tank):
        super().add_tank(tank)

    def __str__(self):
        return TO_STRING_BOT % self.number