from utils.Factory import Factory
from models.game.player.Bot import Bot

class BotFactory(Factory):
    @classmethod
    def create(cls, tank):
        bot:Bot = cls._create(Bot, tank)
        bot.number = cls._number(Bot)
        return bot