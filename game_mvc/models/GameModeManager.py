from enum import Enum
from utils import Observable


class GameMode(Enum):
    ONE_PLAYER = "1 Player"
    TWO_PLAYERS = "2 Players"


class GameModeManager(Observable):
    def __init__(self):
        super().__init__()
        self.__mode = GameMode.ONE_PLAYER

    @property
    def mode(self):
        return self.__mode.value

    def set_mode(self, mode):
        self.__mode = mode
        self.notify_observers(self.mode)

    def set_one_player(self):
        self.set_mode(GameMode.ONE_PLAYER)

    def set_two_players(self):
        self.set_mode(GameMode.TWO_PLAYERS)

    @property
    def is_one_player(self):
        return self.__mode is GameMode.ONE_PLAYER

    @property
    def is_two_players(self):
        return self.__mode is GameMode.TWO_PLAYERS

    @property
    def all_modes(self):
        return GameMode._value2member_map_
