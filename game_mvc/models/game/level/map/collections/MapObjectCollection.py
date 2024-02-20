from utils.Collection import Collection

from models.game.level.map.MapObject import MapObject
from models.game.level.map.MapObjectChar import MapObjectChar
from models.game.level.map.MapObjectPosition import MapObjectPosition

from models.game.level.map.factories.MapObjectFactory import MapObjectFactory

from exceptions.map import (
    NotValidMapObjectException,
    WrongPositionDataException
)

class MapObjectCollection:
    __objects:list[list[MapObject]] = []
    __bot_tanks = {
        MapObjectChar.BOT_TANK.value: []
    }
    __player_tanks = {
        MapObjectChar.PLAYER_ONE.value: None,
        MapObjectChar.PLAYER_TWO.value: None,
    }

    @property
    def bot_tanks(self): return self.__bot_tanks

    @property
    def player_tanks(self): return self.__player_tanks

    def set(self, map_data):
        self.__objects = [[_ for _ in row] for row in map_data]

    def add(self, object, object_char=None):
        if not isinstance(object, MapObject):
            raise NotValidMapObjectException()
        if object_char in self.__bot_tanks:
            self.__bot_tanks[object_char].append(object)
        elif object_char in self.__player_tanks:
            self.__player_tanks[object_char] = object
        self[object.position] = object

    def remove(self, object):
        if not isinstance(object, MapObject):
            raise NotValidMapObjectException()
        self.__objects[object.position.y][object.position.x] = MapObjectFactory.create("0", object.position)

    def __len__(self):
        return len(self.__objects)
    
    def __getitem__(self, position) -> MapObject:
        if not isinstance(position, MapObjectPosition):
            raise WrongPositionDataException()
        return self.__objects[position.y][position.x]
    
    def __setitem__(self, position, object):
        if not isinstance(position, MapObjectPosition):
            raise WrongPositionDataException()
        if not isinstance(object, MapObject):
            raise NotValidMapObjectException()
        self.__objects[position.y][position.x] = object
        
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self) -> list[MapObject]:
        if self.index < len(self.__objects):
            row = self.__objects[self.index]
            self.index += 1
            return row
        raise StopIteration