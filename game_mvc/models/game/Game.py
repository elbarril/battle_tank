from constants.text import TO_STRING_GAME
from constants.game import FIRST_LEVEL, FIRST_PLAYER, SECOND_PLAYER

from models.game.GameStateManager import GameStateManager
from models.game.GameModeManager import GameModeManager

from models.level.Level import Level
from models.player.Player import Player, PlayerOne, PlayerTwo

class Game:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__mode_manager = GameModeManager()
        self.__state_manager = GameStateManager()
        self.__players:dict[int, Player] = {}
        self.__level:Level = None

    @property
    def mode(self):
        return self.__mode_manager.mode
    
    def reset(self):
        self.__state_manager.game_init()
        self.__players:dict[int, Player] = {}
        self.__level:Level = None

    def toggle_players_mode(self):
        if self.__mode_manager.is_one_player:
            self.__mode_manager.set_two_players()
        else:
            self.__mode_manager.set_one_player()

    def load_players(self):
        self.__players.setdefault(FIRST_PLAYER, PlayerOne())
        if self.__mode_manager.is_two_players:
            self.__players.setdefault(SECOND_PLAYER, PlayerTwo())
        self.__state_manager.players_ready()
    
    def load_level(self, number=FIRST_LEVEL):
        self.__level = Level(number)
        self.__level.load_map_data()
        self.__level.add_statics_to_map()
        self.__level.add_player_tanks_to_map(self.players)
        self.__level.add_bot_tanks_to_map()
        self.__state_manager.level_ready()
    
    def play_level(self):
        self.__state_manager.level_start()
    
    def pause_level(self):
        self.__state_manager.level_paused()
    
    @property
    def level(self):
        return self.__level
    
    @property
    def players(self):
        return [player for player in self.__players.values() if player is not None]

    def __str__(self):
        return TO_STRING_GAME % ([str(p) for p in self.players], self.__level, self.__level.map)