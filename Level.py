from Player import Player
from Bot import Bot
from Wall import Wall

from Constants import LEVELS
from Constants import MAP_OBJECT_MAX_SIZE, MAP_OBJECT_MAX_RADIO
from Constants import (
    WALL_MNCODE,
    BOT_MNCODE,
    PLAYER_MNCODE
)

class Level:
    def __init__(self, key:int):
        self.__key = key
        self.__map_objects:dict[str,list] = {
            "walls": [],
            "tanks": [],
            "players": []
        }
        
        for pos_y, row in enumerate(LEVELS[key]):
            for pos_x, map_object_number_code in enumerate(row):
                obj_row = pos_y*MAP_OBJECT_MAX_SIZE
                obj_column = pos_x*MAP_OBJECT_MAX_SIZE
                if map_object_number_code == WALL_MNCODE:
                    self.__map_objects["walls"].append(Wall(obj_row, obj_column))
                elif map_object_number_code == BOT_MNCODE:
                    self.__map_objects["tanks"].append(Bot(obj_row+MAP_OBJECT_MAX_RADIO, obj_column+MAP_OBJECT_MAX_RADIO))
                elif map_object_number_code == PLAYER_MNCODE:
                    self.__map_objects["players"].append(Player(obj_row+MAP_OBJECT_MAX_RADIO, obj_column+MAP_OBJECT_MAX_RADIO))
            
    @property
    def key(self) -> int:
        return self.__key
    
    @property
    def players(self) -> list[Player]:
        return self.__map_objects["players"]
        
    @property
    def bots(self) -> list[Bot]:
        return self.__map_objects["tanks"]
        
    @property
    def walls(self) -> list[Wall]:
        return self.__map_objects["walls"]