from constants.text import TO_STRING_GAME
from constants.game import FIRST_LEVEL, FIRST_PLAYER, SECOND_PLAYER

from models.game.GameStateManager import GameStateManager
from models.game.GameModeManager import GameModeManager

from models.level.Level import Level
from models.player.Player import PlayerOne, PlayerTwo

class Game:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    __players = {}
    __level = None

    def __init__(self):
        self.__mode_manager = GameModeManager()
        self.__state_manager = GameStateManager()

    @property
    def mode(self):
        return self.__mode_manager.mode

    def toggle_players_mode(self):
        if self.__mode_manager.is_one_player_mode:
            self.__mode_manager.set_mode(SECOND_PLAYER)
        else:
            self.__mode_manager.set_mode(FIRST_PLAYER)

    def load_players(self):
        self.__players.setdefault(FIRST_PLAYER, PlayerOne())
        if self.__mode_manager.is_two_player_mode:
            self.__players.setdefault(SECOND_PLAYER, PlayerTwo())
    
    def load_level(self, number=FIRST_LEVEL):
        self.__level = Level(number)
        self.__level.load_map_data()
        self.__state_manager.level_ready()

    def load_map(self):
        self.level.add_statics_to_map()
        self.level.add_player_tanks_to_map(self.players)
        self.level.add_bot_tanks_to_map()
    
    def play_level(self):
        self.__state_manager.level_start()
    
    @property
    def level(self):
        return self.__level
    
    @property
    def players(self):
        return [player for player in self.__players.values() if player is not None]

    def __str__(self):
        return TO_STRING_GAME % (self.players, self.__level)