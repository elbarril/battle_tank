from utils.Factory import Factory
from models.game.Level import Level

class LevelFactory(Factory):
    @classmethod
    def create(cls) -> Level:
        number = cls._next_number(Level)
        level = cls._create(Level, number)
        return level