from Tank import Tank
from Constants import (
    PLAYER_TANK_IMAGE_FILENAME,
    MAP_OBJECT_MAX_SIZE,
    MAP_OBJECT_MAX_RADIO
)

class Player:
    def __init__(self, row:int, column:int, directions:dict[str,tuple[int|str]], shoot_keys:list[str]):
        self.__tank = Tank(row+MAP_OBJECT_MAX_RADIO, column+MAP_OBJECT_MAX_RADIO, MAP_OBJECT_MAX_SIZE, PLAYER_TANK_IMAGE_FILENAME)
        self.__is_alive = True
        self.__directions = directions
        self.__shoot_keys = shoot_keys

    @property
    def tank(self) -> Tank:
        return self.__tank
    
    @property
    def is_alive(self) -> bool:
        return self.__is_alive

    def die(self):
        self.__is_alive = False

    @property
    def shoot_keys(self) -> list[str]:
        return self.__shoot_keys

    @property
    def directions(self) -> dict[str,tuple[int|str]]:
        return self.__directions