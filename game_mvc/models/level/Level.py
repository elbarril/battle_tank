from csv import reader
from os import walk

from models.player.Player import Player

from models.map.Map import Map
from models.map.MapObject import MapObject
from models.map.MapObjectType import MapObjectType
from models.map.MapObjectCompound import MapObjectCompound
from models.map.MapPosition import MapPosition
from models.map.MapObjectSize import MapObjectSize

from models.level.MapObjectCreator import MapObjectCreator

from constants.text import TO_STRING_LEVEL
from constants.map import MAP_COLUMN_POSITIONS, MAP_ROW_POSITIONS, MAPS_PATH, MAPS_FILENAME_PREFIX, MAPS_FILE_EXTENSION
from constants.game import FIRST_LEVEL, MAX_LEVEL_NUMBER

LEVEL_MAP_FILES = [level_map_file_path for level_map_file_path in next(walk(MAPS_PATH), (None, None, []))[2]]

class Level(MapObjectCreator):
    def __init__(self, level_number:int) -> None:
        if not isinstance(level_number, int):
            raise TypeError(f"Wrong level number type: {level_number}")
        if not level_number >= FIRST_LEVEL or level_number > MAX_LEVEL_NUMBER:
            raise ValueError(f"Level number should be between {FIRST_LEVEL} and {MAX_LEVEL_NUMBER}.\nNumber: {level_number}")
        self.__number = level_number
        self.__map = Map()

    def load_map_data(self):
        level_number_string = str(self.__number).zfill(2)
        map_file = MAPS_FILENAME_PREFIX + level_number_string + MAPS_FILE_EXTENSION

        if not map_file in LEVEL_MAP_FILES:
            raise FileNotFoundError(f"Level {level_number_string} doesn't have map file in '{MAPS_PATH}'.")

        with open(MAPS_PATH + map_file, mode="r") as map_file:
            map_matrix = reader(map_file)
            for y, row in enumerate(map_matrix):
                for x, object_type in enumerate(row):
                    object_type = MapObjectType(object_type)
                    position = MapPosition(x*MAP_COLUMN_POSITIONS, y*MAP_ROW_POSITIONS)
                    size = MapObjectSize(MAP_COLUMN_POSITIONS, MAP_ROW_POSITIONS)
                    self._create_map_object(object_type, position, size)

    def add_static_tanks_to_map(self):
        for static in self._statics:
            self.__add_object_to_map(static)
            
    def add_bot_tanks_to_map(self):
        for bot in self._bots:
            self.__add_object_to_map(bot.tank)

    def add_player_tanks_to_map(self, players:list[Player]):
        for player in players:
            player_tank = self._player_tanks[player.number]
            player.add_tank(player_tank)
            self.__add_object_to_map(player_tank)

    def __add_object_to_map(self, object:MapObject) -> None:
        if isinstance(object, MapObjectCompound):
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

    def __str__(self):
        return TO_STRING_LEVEL % str(self.__number)