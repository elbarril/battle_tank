from utils.Factory import Factory
from models.game.Level import Level

class LevelFactory(Factory):
    @classmethod
    def create(cls, level_number) -> Level:
        level = cls._create(Level, level_number)
        return level