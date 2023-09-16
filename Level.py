from Player import Player
from PlayerOne import PlayerOne
from PlayerTwo import PlayerTwo
from Bot import Bot
from Wall import Wall

from Constants import LEVEL_MAP
from Constants import MAP_OBJECT_MAX_SIZE, MAP_OBJECT_MAX_RADIO
from Constants import (
    WALL_MNCODE,
    BOT_MNCODE,
    PLAYER1_MNCODE,
    PLAYER2_MNCODE
)

LEVEL_MAP_TYPE= {
    WALL_MNCODE: Wall,
    BOT_MNCODE: Bot,
    PLAYER1_MNCODE: PlayerOne,
    PLAYER2_MNCODE: PlayerTwo
}

class Level:
    def __init__(self, id:int):
        self.__id = id

        self.__map_objects:dict[int,list] = {key:[] for key in LEVEL_MAP_TYPE.keys()}

    def create_map(self):
        for Y, ROWS in enumerate(LEVEL_MAP[self.__id]):
            for X, MNCODE in enumerate(ROWS):
                map_type = LEVEL_MAP_TYPE.get(MNCODE)
                if map_type:
                    map_object:map_type = map_type(
                        row = Y * MAP_OBJECT_MAX_SIZE + MAP_OBJECT_MAX_RADIO,
                        column = X * MAP_OBJECT_MAX_SIZE + MAP_OBJECT_MAX_RADIO
                    )
                    self.__map_objects[MNCODE].append(map_object)
    @property
    def has_next(self) -> bool:
        return True if LEVEL_MAP.get(self.__id + 1) else False

    @property
    def next_level_id(self) -> int:
        return self.__id + 1

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def players(self) -> list[Player]:
        players = self.__map_objects[PLAYER1_MNCODE] + self.__map_objects[PLAYER2_MNCODE]
        return players
        
    @property
    def bots(self) -> list[Bot]:
        return self.__map_objects[BOT_MNCODE]
        
    @property
    def walls(self) -> list[Wall]:
        return self.__map_objects[WALL_MNCODE]