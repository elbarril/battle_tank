
from constants.game import FIRST_PLAYER, SECOND_PLAYER

from enum import Enum
class GameMode(Enum):
    ONE_PLAYER = FIRST_PLAYER
    TWO_PLAYERS = SECOND_PLAYER

class GameModeManager:
    def __init__(self):
        self.__mode = GameMode.ONE_PLAYER

    @property
    def mode(self):
        return self.__mode.value

    def set_one_player(self):
        self.__mode = GameMode.ONE_PLAYER

    def set_two_players(self):
        self.__mode = GameMode.TWO_PLAYERS

    @property
    def is_one_player(self):
        return self.__mode is GameMode.ONE_PLAYER

    @property
    def is_two_players(self):
        return self.__mode is GameMode.TWO_PLAYERS