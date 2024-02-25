from string import digits

from utils.Singleton import Singleton

from models.game.factories.PlayerFactory import PlayerFactory, Player
from models.game.factories.LevelFactory import LevelFactory

from constants.text import TO_STRING_GAME
from constants.level import FIRST_LEVEL

from exceptions.game import LevelDoesNotExistsException

from models.GameStateManager import GameStateManager
from models.GameModeManager import GameModeManager

class Game(Singleton):
    __player_one = None
    __player_two = None
    __level = None

    def __init__(self):
        self.__mode_manager = GameModeManager()
        self.__state_manager = GameStateManager()

    def toggle_players_mode(self):
        if not self.__state_manager.is_game_init:
            return Exception(f"Cannot create players. Game state: {self.__state_manager.state}")
        if self.__mode_manager.is_one_player_mode:
            self.__mode_manager.two_players()
        else:
            self.__mode_manager.one_player()

    def create_players(self):
        if not self.__state_manager.is_game_init:
            return Exception(f"Cannot create players. Game state: {self.__state_manager.state}")
        self.__player_one = PlayerFactory.create(1)
        if self.__mode_manager.is_two_player_mode:
            self.__player_two = PlayerFactory.create(2)
        self.__state_manager.players_ready()
    
    def new_level(self, level_number=FIRST_LEVEL):
        if not self.__state_manager.is_players_ready:
            return Exception("No players.")
        self.__level = LevelFactory.create(level_number)
        self.__level.load_map()
        self.__player_one.add_tank(self.__level.player_tank_one)
        if self.__mode_manager.is_two_player_mode:
            self.__player_two.add_tank(self.__level.player_tank_two)
        self.__state_manager.level_ready()
        return self.__level
    
    def play_level(self):
        if not self.__state_manager.is_level_ready:
            return Exception("Level is not ready.")
        self.__level.map.add_object(self.__level.player_tank_one)
        if self.__mode_manager.is_two_player_mode:
            self.__level.map.add_object(self.__level.player_tank_two)
        for bot in self.__level.bots:
            self.__level.map.add_object(bot.tank)
        self.__state_manager.level_start()
    
    @property
    def level(self):
        if self.__level is None:
            return LevelDoesNotExistsException()
        return self.__level
    
    @property
    def players(self) -> list[Player]:
        return [player for player in [self.__player_one, self.__player_two] if player]

    def __str__(self):
        return TO_STRING_GAME % (self.players, self.__level)