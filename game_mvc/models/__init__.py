from .map import Map
from .level import Level
from utils.Singleton import Singleton
from .GameModeManager import GameModeManager
from .GameStateManager import GameStateManager
from .player import HumanPlayer, PlayerOne, PlayerTwo


class Game(Singleton):
    def __init__(self):
        self.__mode_manager = GameModeManager()
        self.__state_manager = GameStateManager()

        self.__players: dict[int, HumanPlayer] = {}
        self.__level: Level = None
        self.__map: Map = None

    def restart(self):
        self.__mode_manager.set_one_player()
        self.__state_manager.game_init()
        self.__players: dict[int, HumanPlayer] = {}
        self.__level: Level = None
        self.__map: Map = None

    def toggle_players_mode(self):
        if self.__mode_manager.is_one_player:
            self.__mode_manager.set_two_players()
        else:
            self.__mode_manager.set_one_player()

    def load_players(self):
        self.__players.setdefault(1, PlayerOne())
        if self.__mode_manager.is_two_players:
            self.__players.setdefault(2, PlayerTwo())
        self.__state_manager.players_ready()

    def load_level(self, number=1):
        self.__level = Level(number)
        self.__level.create_level_objects()
        self.__state_manager.level_ready()

    def load_map(self):
        self.__map = Map()

        for static in self.__level.statics:
            if static.position*static.size in self.__map:
                self.__map[static.position*static.size] = static

        for player_tank in self.__level.player_tanks:
            if player_tank.player_number in self.__players:
                self.__players[player_tank.player_number].set_tank(player_tank)
                if player_tank.position*player_tank.size in self.__map:
                    self.__map[player_tank.position *
                               player_tank.size] = player_tank

        for bot_tank in self.__level.bot_tanks:
            if bot_tank.position*bot_tank.size in self.__map:
                self.__map[bot_tank.position*bot_tank.size] = bot_tank

    def play_level(self):
        self.__state_manager.level_playing()

    def pause_level(self):
        self.__state_manager.level_paused()

    @property
    def mode(self):
        return self.__mode_manager.mode

    @property
    def level(self):
        return self.__level

    @property
    def map(self):
        return self.__map

    @property
    def players(self):
        return [player for player in self.__players.values() if player is not None]
