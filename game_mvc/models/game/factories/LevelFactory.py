from models.game.Level import Level
from utils.Factory import Factory

class LevelFactory(Factory):
    @classmethod
    def new(cls, players) -> Level:
        next = cls._next_number(Level)
        level = cls._create(Level, next, players)
        return level