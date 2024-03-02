from models.map.Map import Map
from models.map.MapDataReader import MapDataReader

from models.factories.BotFactory import BotFactory
from models.factories.MapObjectFactory import MapObjectFactory

from models.collections.BotCollection import BotCollection

from models.level.LevelNumber import LevelNumber

from models.map.MapObject import MapObject
from models.map.MapObjectType import MapObjectType

from constants.text import TO_STRING_LEVEL
from constants.map import MAP_POSITION_HEIGHT, MAP_POSITION_WIDTH

class Level:
    def __init__(self, number):
        self.__object_handler = {
            MapObjectType.PLAYER_ONE: self.__set_player_one_tank,
            MapObjectType.PLAYER_TWO: self.__set_player_two_tank,
            MapObjectType.BOT_TANK: self.__create_bot,
            MapObjectType.BRICK: self.__add_object_to_map,
            MapObjectType.FLUID: self.__add_object_to_map
        }

        self.__map = Map()
        self.__number = LevelNumber(number)
        self.__bots = BotCollection()
        self.__player_one_tank = None
        self.__player_two_tank = None

    def load_map(self):
        map_data = MapDataReader.read(self.__number)
        for y, row in enumerate(map_data):
            for x, object_type in enumerate(row):
                map_object = MapObjectFactory.create(object_type, x*MAP_POSITION_WIDTH, y*MAP_POSITION_HEIGHT)
                object_handler = self.__object_handler[object_type]
                object_handler(map_object)

    def __add_object_to_map(self, object:MapObject):
        for position in object.position:
            self.__map[position] = object

    def __add_fluid_to_map(self, position):
        for position in position:
            self.__add_object_to_map(MapObjectFactory.create(MapObjectType.FLUID, position.x, position.y))

    def __set_player_one_tank(self, tank):
        self.__player_one_tank = tank
        self.__add_fluid_to_map(tank.position)

    def __set_player_two_tank(self, tank):
        self.__player_two_tank = tank
        self.__add_fluid_to_map(tank.position)

    def __create_bot(self, tank):
        bot = BotFactory.create(tank)
        self.__bots.add(bot)
        self.__add_fluid_to_map(tank.position)

    def load_player_one(self):
        self.__add_object_to_map(self.__player_one_tank)

    def load_player_two(self):
        self.__add_object_to_map(self.__player_two_tank)

    def load_bots(self):
        for bot in self.__bots:
            self.__add_object_to_map(bot.tank)

    @property
    def player_one_tank(self):
        return self.__player_one_tank

    @property
    def player_two_tank(self):
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