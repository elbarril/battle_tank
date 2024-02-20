import csv

from models.game.level.map.MapFilePath import MapFilePath
from models.game.level.map.MapObjectPosition import MapObjectPosition

from models.game.level.map.collections.MapObjectCollection import MapObjectCollection

from models.game.level.map.factories.MapObjectFactory import MapObjectFactory

from exceptions.map import (
    MapDataHasNotRowsException,
    WrongPositionDataException
)

class Map:
    __objects = MapObjectCollection()
    __map_data:list[list[str]] = None

    def __init__(self, map_data):
        if not (isinstance(map_data, list) and len(map_data)):
            raise MapDataHasNotRowsException()
        self.__map_data = map_data
        self.__objects.set(map_data)

    @classmethod
    def read(cls, level_number):
        with open(MapFilePath(level_number), mode="r") as level_map_file:
            map_data = list(list(row) for row in csv.reader(level_map_file))
        return cls(map_data)
    
    def create(self):
        for row, columns in enumerate(self.__map_data):
            for column, object_char in enumerate(columns):
                position = MapObjectPosition(column,row)
                map_object = MapObjectFactory.create(object_char, position)
                self.__objects.add(map_object, object_char)
    
    def is_valid_position(self, position):
        if not isinstance(position, MapObjectPosition):
            raise WrongPositionDataException()
        x,y = position.x, position.y
        return y >= 0 and y < len(self.__map_data) and x >= 0 and x < len(self.__map_data[y])

    def collision(self, position):
        return self.__objects[position].is_solid

    def add_object(self, object):
        self.__objects.add(object)

    def remove_object(self, object):
        self.__objects.remove(object)

    @property
    def player_tanks(self):
        return self.__objects.player_tanks

    @property
    def bot_tanks(self):
        return self.__objects.bot_tanks

    def __iter__(self):
        return iter(self.__objects)