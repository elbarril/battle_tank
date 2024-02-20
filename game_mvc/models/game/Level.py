from models.game.level.LevelNumber import LevelNumber
from models.game.factories.BotFactory import BotFactory
from models.game.collections.BotCollection import BotCollection
from models.game.level.Map import Map
from constants.level import TO_STRING, FIRST_LEVEL
from exceptions.level import MapDoesNotExistsException

class Level:
    __number = None
    __map = None

    def __init__(self, number=FIRST_LEVEL):
        self.__number = LevelNumber(number)
        self.__bots = BotCollection()

    def load_map(self):
        self.__map = Map.read(self.__number)
        return self.__map

    def load_bots(self):
        if self.__map is None:
            raise MapDoesNotExistsException()
        from models.game.level.map.MapObjectChar import MapObjectChar
        for bot_tank in self.__map.bot_tanks[MapObjectChar.BOT_TANK.value]:
            bot = BotFactory.create(bot_tank)
            self.__bots.add(bot)
            self.__map.add_object(bot.tank)

    @property
    def map(self):
        if self.__map is None:
            raise MapDoesNotExistsException()
        return self.__map
    
    @property
    def bots(self):
        return self.__bots
    
    @property
    def number(self):
        return self.__number

    def __str__(self):
        return TO_STRING % str(self.__number)