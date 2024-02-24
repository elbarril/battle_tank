from models.game.player.AbstractPlayer import AbstractPlayer
from constants.text import TO_STRING_BOT

class Bot(AbstractPlayer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_bot = True

    def add_tank(self, tank):
        super().add_tank(tank)

    def __str__(self):
        return TO_STRING_BOT % self.number