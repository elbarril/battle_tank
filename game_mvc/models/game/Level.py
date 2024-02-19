from models.game.level.LevelNumber import LevelNumber
from models.game.level.Map import Map
from constants.level import TO_STRING, FIRST_LEVEL
from exceptions.level import MapDoesNotExistsException

class Level:
    number = None
    __map = None

    def __init__(self, number=FIRST_LEVEL, players=[]):
        self.number = LevelNumber(number)

    def load_map(self):
        self.__map = Map.read(self.number)
        return self.__map

    @property
    def map(self):
        if self.__map is None:
            raise MapDoesNotExistsException()
        return self.__map

    def __str__(self):
        return TO_STRING % str(self.number)