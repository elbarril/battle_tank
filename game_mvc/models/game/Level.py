
from models.game.factories.BotFactory import BotFactory
from models.game.collections.BotCollection import BotCollection
from models.game.collections.PlayerCollection import PlayerCollection

from models.game.level.MapDataReader import MapDataReader
from models.game.level.LevelNumber import LevelNumber
from models.game.level.Map import Map

from models.game.level.map.factories.MapObjectFactory import MapObjectFactory, MapObjectType
from constants.level import TO_STRING, FIRST_LEVEL

class Level:
    __map = Map()

    def __init__(self, number=FIRST_LEVEL):
        self.__number = LevelNumber(number)
        self.__bots = BotCollection()

    def load_map(self, players:PlayerCollection):
        map_data = MapDataReader.read(self.__number)
        for y,row in enumerate(map_data):
            self.__map.add_row()
            for x,object_type in enumerate(row):
                map_object = MapObjectFactory.create(object_type, x, y)
                self.__map[y].add(map_object)

                if object_type is MapObjectType.PLAYER_ONE and len(players):
                    players[0].add_tank(map_object)
                elif object_type is MapObjectType.PLAYER_TWO and len(players) > 1:
                    players[1].add_tank(map_object)
                elif object_type is MapObjectType.BOT_TANK:
                    bot = BotFactory.create(map_object)
                    self.__bots.add(bot)

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
        return TO_STRING % str(self.__number)