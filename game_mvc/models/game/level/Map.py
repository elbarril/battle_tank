import csv

from models.game.level.map.collection.MapObjectCollection import MapObjectCollection
from models.game.level.map.MapFilePath import MapFilePath

class Map:
    def __init__(self, map_data):
        self.__objects = MapObjectCollection(map_data)

    @classmethod
    def read(cls, level_number):
        with open(MapFilePath(level_number), mode="r") as level_map_file:
            map_data = list(list(row) for row in csv.reader(level_map_file))
        return cls(map_data)
    
    def create(self, player_1=None, player_2=None):
        return self.__objects.create(player_1, player_2)
    
    def is_valid_position(self, position):
        return self.__objects.is_valid_position(position)

    def collision(self, position):
        return self.__objects[position].is_solid

    def add_object(self, object):
        self.__objects.add(object)

    def remove_object(self, object):
        self.__objects.remove(object)

    def __iter__(self):
        return iter(self.__objects)