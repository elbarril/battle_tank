from models.game.level.LevelNumber import LevelNumber
from models.game.factories.BotFactory import BotFactory
from models.game.collections.BotCollection import BotCollection
from models.game.level.Map import Map
from constants.level import TO_STRING, FIRST_LEVEL
from exceptions.level import MapDoesNotExistsException

class Level:
    number = None
    __map = None

    def __init__(self, number=FIRST_LEVEL):
        self.number = LevelNumber(number)
        self.__bots = BotCollection()

    def load_map(self):
        self.__map = Map.read(self.number)
        return self.__map

    def load_bots(self):
        for bot_tank in self.__map.bots:
            bot = BotFactory.create(bot_tank)
            self.__bots.add(bot)

    @property
    def map(self):
        if self.__map is None:
            raise MapDoesNotExistsException()
        return self.__map
    
    @property
    def bots(self):
        return self.__bots

    def __str__(self):
        return TO_STRING % str(self.number)