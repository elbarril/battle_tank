from models.game.collections.PlayerCollection import PlayerCollection, Player

from models.game.level.map.MapObject import MapObject
from models.game.level.map.factories.MapObjectFactory import MapObjectFactory
from models.game.level.map.MapObjectPosition import MapObjectPosition

from exceptions.map import (
    MapDataHasNotRowsException,
    NotValidMapObjectException,
    WrongPositionDataException
)

class MapObjectCollection:
    __map_data:list[list[str]] = []
    __objects:list[list[MapObject]] = []
    __players:dict[str,Player] = {
        "O": None,
        "T": None
    }

    def __init__(self, map_data):
        if not (isinstance(map_data, list) and len(map_data)):
            raise MapDataHasNotRowsException()
        self.__map_data = map_data
    
    def create(self, player_1:Player, player_2:Player):
        if player_1: self.__players["O"] = player_1
        if player_2: self.__players["T"] = player_2
        for row, columns in enumerate(self.__map_data):
            self.__objects.append(columns)
            for column, object in enumerate(columns):
                position = MapObjectPosition(column,row)
                player = self.__players.get(object)
                if player:
                    self.__objects[row][column] = player.create_tank(position)
                else:
                    self.__objects[row][column] = MapObjectFactory.create(object, position)

    def add(self, object):
        if not isinstance(object, MapObject):
            raise NotValidMapObjectException()
        self.__objects[object.position.y][object.position.x] = object

    def remove(self, object):
        if not isinstance(object, MapObject):
            raise NotValidMapObjectException()
        self.__objects[object.position.y][object.position.x] = MapObjectFactory.create("0", object.position)

    def is_valid_position(self, position):
        if not isinstance(position, MapObjectPosition):
            raise WrongPositionDataException()
        x,y = position.x, position.y
        return y >= 0 and y < len(self.__objects) and x >= 0 and x < len(self.__objects[y])

    def __len__(self):
        return len(self.__objects)
    
    def __getitem__(self, position) -> MapObject:
        if not isinstance(position, MapObjectPosition):
            raise WrongPositionDataException()
        return self.__objects[position.y][position.x]
        
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.__objects):
            row = self.__objects[self.index]
            self.index += 1
            return row
        raise StopIteration