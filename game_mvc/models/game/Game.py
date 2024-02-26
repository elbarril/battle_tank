from utils.Singleton import Singleton

from models.factories.PlayerFactory import PlayerFactory
from models.factories.LevelFactory import LevelFactory

from constants.text import TO_STRING_GAME
from constants.game import FIRST_LEVEL

from models.game.GameStateManager import GameStateManager
from models.game.GameModeManager import GameModeManager

class Game(Singleton):
    __player_one = None
    __player_two = None
    __level = None

    def __init__(self):
        self.__mode_manager = GameModeManager()
        self.__state_manager = GameStateManager()

    @property
    def mode(self):
        return self.__mode_manager.mode_value

    def toggle_players_mode(self):
        if self.__mode_manager.is_one_player_mode:
            self.__mode_manager.two_players()
        else:
            self.__mode_manager.one_player()

    def __create_player_one(self):
        self.__player_one = PlayerFactory.create(1)
        self.__player_one.add_tank(self.__level.player_one_tank)
        self.__level.load_player_one()

    def __create_player_two(self):
        self.__player_two = PlayerFactory.create(2)
        self.__player_two.add_tank(self.__level.player_two_tank)
        self.__level.load_player_two()

    def create_players(self):
        self.__create_player_one()
        if self.__mode_manager.is_two_player_mode:
            self.__create_player_two()
        self.__state_manager.players_ready()
    
    def new_level(self, number=FIRST_LEVEL):
        self.__level = LevelFactory.create(number)
        self.__level.load_map()
        self.__state_manager.level_ready()
        return self.__level
    
    def play_level(self):
        self.__level.load_bots()
        self.__state_manager.level_start()
    
    @property
    def level(self):
        return self.__level
    
    @property
    def players(self):
        return [player for player in [self.__player_one, self.__player_two] if player is not None]

    def __str__(self):
        return TO_STRING_GAME % (self.players, self.__level)