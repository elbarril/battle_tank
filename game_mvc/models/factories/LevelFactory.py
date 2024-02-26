from utils.Factory import Factory
from models.level.Level import Level

class LevelFactory(Factory):
    @classmethod
    def create(cls, number) -> Level:
        level = cls._create(Level, number)
        return level