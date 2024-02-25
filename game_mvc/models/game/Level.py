from models.game.factories.BotFactory import BotFactory
from models.game.collections.BotCollection import BotCollection

from models.game.level.MapDataReader import MapDataReader
from models.game.level.LevelNumber import LevelNumber
from models.game.level.Map import Map

from models.game.level.map.factories.MapObjectFactory import MapObjectFactory, MapObjectType
from constants.text import TO_STRING_LEVEL

class Level:
    def __init__(self, number):
        self.__map = Map()
        self.__number = LevelNumber(number)
        self.__bots = BotCollection()
        self.__player_one_tank = None
        self.__player_two_tank = None

    def load_map(self):
        map_data = MapDataReader.read(self.__number)
        for y,row in enumerate(map_data):
            self.__map.add_row()
            for x,object_type in enumerate(row):
                map_object = MapObjectFactory.create(object_type, x, y)
                if object_type in [MapObjectType.PLAYER_ONE, MapObjectType.PLAYER_TWO, MapObjectType.BOT_TANK]:
                    if object_type is MapObjectType.PLAYER_ONE:
                        self.__player_one_tank = map_object
                    elif object_type is MapObjectType.PLAYER_TWO:
                        self.__player_two_tank = map_object
                    elif object_type is MapObjectType.BOT_TANK:
                        bot = BotFactory.create(map_object)
                        self.__bots.add(bot)
                    self.__map[y].add(MapObjectFactory.create_empty(x, y))
                else:
                    self.__map[y].add(map_object)

    @property
    def player_tank_one(self):
        return self.__player_one_tank

    @property
    def player_tank_two(self):
        return self.__player_two_tank

    @property
    def map(self):
        return self.__map
    
    @property
    def bots(self):
        return self.__bots
    
    @property
    def number(self):
        return self.__number

    def __str__(self):
        return TO_STRING_LEVEL % str(self.__number)