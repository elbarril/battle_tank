from os import walk
from csv import reader

from ..map import Map
from ..map import MapPosition
from ..player import HumanPlayer
from ..map.object import MapObject
from ..player import BotPlayerCollection
from ..map.object.MapObjectType import *
from ..map.object.MapObjectSize import MapObjectSize
from ..map.object.abstract.CompoundMapObject import CompoundMapObject

LEVEL_MAP_FILES = [map_file_path for map_file_path in next(
    walk("./maps/"), (None, None, []))[2]]


class Level:
    def __init__(self, number: int) -> None:
        if not isinstance(number, int):
            raise TypeError(f"Wrong level number type: {number}")
        if not number >= 1 or number > 99:
            raise ValueError(
                f"Level number should be between {1} and {99}.\nNumber: {number}")
        self.__number = number

        self.__player_tanks: set[MapObject] = set()
        self.__bot_tanks: set[MapObject] = set()
        self.__statics: set[MapObject] = set()

        self.__bot = BotPlayerCollection()

    def create_level_objects(self):
        number_string = str(self.__number).zfill(2)
        map_file = "level_" + number_string + ".csv"

        if not map_file in LEVEL_MAP_FILES:
            raise FileNotFoundError(
                f"Level {number_string} doesn't have map file in './maps/'.")

        with open("./maps/" + map_file, mode="r") as map_file:
            map_rows = reader(map_file)
            for y, row in enumerate(map_rows):
                for x, object_type in enumerate(row):
                    object_type_code = MapObjectTypeCode(object_type)
                    object_type = MAP_OBJECT_TYPES[object_type_code]
                    if object_type:
                        position = MapPosition(x*4, y*4)
                        size = MapObjectSize(4, 4)
                        map_object = object_type.create(position, size)

                        if object_type_code in PLAYER_TANK_TYPES:
                            self.__player_tanks.add(map_object)
                        elif object_type_code in BOT_TANK_TYPES:
                            self.__bot_tanks.add(map_object)
                        elif object_type_code in STATIC_TYPES:
                            self.__statics.add(map_object)

    def add_statics_to_map(self):
        for static in self.__statics:
            if static:
                self.__add_object_to_map(static)

    def add_bot_tanks_to_map(self):
        for bot_tank in self.__bot_tanks:
            self.__bot.set_bot(bot_tank)
            self.__add_object_to_map(bot_tank)

    def add_player_tanks_to_map(self, players: list[HumanPlayer]):
        for player in players:
            player_tanks = [
                tank for tank in self.__player_tanks if tank.player_number == player.number]
            if player_tanks:
                player.set_tank(player_tanks[0])
                self.__add_object_to_map(player_tanks[0])

    def __add_object_to_map(self, object: MapObject) -> None:
        if isinstance(object, CompoundMapObject):
            for obj in object:
                self.__add_object_to_map(obj)
        elif object.position*object.size in self.__map:
            self.__map[object.position*object.size] = object

    @property
    def statics(self):
        return self.__statics

    @property
    def player_tanks(self):
        return self.__player_tanks

    @property
    def bot_tanks(self):
        return self.__bot_tanks

    @property
    def number(self) -> int:
        return self.__number
