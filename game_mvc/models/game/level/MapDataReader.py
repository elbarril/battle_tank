import csv

from models.game.level.LevelNumber import LevelNumber
from models.game.level.map.MapFilePath import MapFilePath
from models.game.level.map.MapObjectType import MapObjectType

class MapDataReader:
    @classmethod
    def read(cls, level_number:LevelNumber):
        with open(MapFilePath(level_number), mode="r") as map_file:
            map_data = list(list(MapObjectType(type) for type in row) for row in csv.reader(map_file))
        return map_data