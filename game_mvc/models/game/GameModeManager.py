
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

    def set_mode(self, new_mode):
        self.__mode = GameMode(new_mode)

    @property
    def is_one_player_mode(self):
        return self.__mode is GameMode.ONE_PLAYER

    @property
    def is_two_player_mode(self):
        return self.__mode is GameMode.TWO_PLAYERS