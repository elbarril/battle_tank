from utils.Factory import Factory
from models.player.Bot import Bot

class BotFactory(Factory):
    @classmethod
    def create(cls, tank):
        bot:Bot = cls._create(Bot, tank)
        return bot