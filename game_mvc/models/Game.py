from utils.Singleton import Singleton

from models.game.factories.PlayerFactory import PlayerFactory, Player
from models.game.factories.LevelFactory import LevelFactory

from constants.text import TO_STRING_GAME
from constants.game import FIRST_LEVEL

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
        if self.__mode_manager.is_one_player_mode:
            self.__mode_manager.two_players()
        else:
            self.__mode_manager.one_player()

    def create_players(self):
        self.__player_one = PlayerFactory.create(1)
        if self.__mode_manager.is_two_player_mode:
            self.__player_two = PlayerFactory.create(2)
        self.__state_manager.players_ready()
    
    def new_level(self, level_number=FIRST_LEVEL):
        self.__level = LevelFactory.create(level_number)
        self.__level.load_map()
        self.__player_one.add_tank(self.__level.player_tank_one)
        if self.__mode_manager.is_two_player_mode:
            self.__player_two.add_tank(self.__level.player_tank_two)
        self.__state_manager.level_ready()
        return self.__level
    
    def play_level(self):
        self.__level.map.add_object(self.__level.player_tank_one)
        if self.__mode_manager.is_two_player_mode:
            self.__level.map.add_object(self.__level.player_tank_two)
        for bot in self.__level.bots:
            self.__level.map.add_object(bot.tank)
        self.__state_manager.level_start()
    
    @property
    def level(self):
        return self.__level
    
    @property
    def players(self) -> list[Player]:
        return [player for player in [self.__player_one, self.__player_two] if player]

    def __str__(self):
        return TO_STRING_GAME % (self.players, self.__level)