from csv import reader
from os import walk

from models.player import BotPlayerCollection
from models.player import HumanPlayer

from models.map import Map
from models.map.MapObject import MapObject
from models.map.MapObjectType import MapObjectType
from models.map.CompoundMapObject import CompoundMapObject
from models.map.MapPosition import MapPosition
from models.map.MapObjectSize import MapObjectSize

from models.level.MapObjectCreator import MapObjectCreator

LEVEL_MAP_FILES = [map_file_path for map_file_path in next(walk("./maps/"), (None, None, []))[2]]

class Level(MapObjectCreator):
    def __init__(self, number:int) -> None:
        if not isinstance(number, int):
            raise TypeError(f"Wrong level number type: {number}")
        if not number >= 1 or number > 99:
            raise ValueError(f"Level number should be between {1} and {99}.\nNumber: {number}")
        self.__number = number
        self.__map = Map()
        self.__bot = BotPlayerCollection()

    def load_map_data(self):
        number_string = str(self.__number).zfill(2)
        map_file = "level_" + number_string + ".csv"

        if not map_file in LEVEL_MAP_FILES:
            raise FileNotFoundError(f"Level {number_string} doesn't have map file in './maps/'.")

        with open("./maps/" + map_file, mode="r") as map_file:
            map_matrix = reader(map_file)
            for y, row in enumerate(map_matrix):
                for x, object_type in enumerate(row):
                    object_type = MapObjectType(object_type)
                    position = MapPosition(x*2, y*2)
                    size = MapObjectSize(2, 2)
                    self._create_map_object(object_type, position, size)

    def add_statics_to_map(self):
        for static in self._statics:
            self.__add_object_to_map(static)
            
    def add_bot_tanks_to_map(self):
        for bot_tank in self._bot_tanks:
            self.__bot.set_bot(bot_tank)
            self.__add_object_to_map(bot_tank)

    def add_player_tanks_to_map(self, players:list[HumanPlayer]):
        for player in players:
            player_tank = self._player_tanks[player.number]
            player.set_tank(player_tank)
            self.__add_object_to_map(player_tank)

    def __add_object_to_map(self, object:MapObject) -> None:
        if isinstance(object, CompoundMapObject):
            for obj in object:
                self.__add_object_to_map(obj)
        else:
            self.__map[object.position*object.size] = object

    @property
    def map(self) -> Map:
        return self.__map
    
    @property
    def number(self) -> int:
        return self.__number