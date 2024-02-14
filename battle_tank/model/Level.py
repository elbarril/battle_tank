from model.MapObject import MapObject, Position
from model.Tank import Tank
from model.Wall import Wall

from constants import (
    PLAYER_MAP_CODE,
    BOT_MAP_CODE,
    WALL_MAP_CODE,
    LEVEL_MAPS,
    MAP_OBJECTS,
    COLUMN_WIDTH,
    ROW_HEIGHT
)

class Level:
    __map_objects_classes = {
        PLAYER_MAP_CODE: Tank,
        BOT_MAP_CODE: Tank,
        WALL_MAP_CODE: Wall
    }

    def __init__(self, id:int):
        MAP = LEVEL_MAPS[id]
        self.__map_objects:dict[int,MapObject] = {MAP_CODE:[] for MAP_CODE in MAP_OBJECTS}

        for row in range(len(MAP)):
            for column in range(len(MAP[row])):
                map_object:MapObject = None
                map_code = MAP[row][column]
                if map_code:
                    position = Position(x=column*COLUMN_WIDTH, y=row*ROW_HEIGHT)
                    map_object = self.__create_map_object(map_code, position)
                    self.__map_objects[map_code].append(map_object)

    @property
    def map_objects(self): return list(self.__map_objects.values())

    @property
    def player_tanks(self): return self.__map_objects[PLAYER_MAP_CODE]

    @property
    def bot_tanks(self): return self.__map_objects[BOT_MAP_CODE]

    @classmethod
    def __create_map_object(cls, map_code:int, position:Position):
        return cls.__map_objects_classes[map_code](position) 