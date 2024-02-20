from utils.Singleton import Singleton

from models.game.GameState import GameState

from models.game.factories.PlayerFactory import PlayerFactory
from models.game.factories.LevelFactory import LevelFactory

from models.game.collections.PlayerCollection import PlayerCollection

from constants.game import *
from exceptions.game import *

class Game(Singleton):
    __level = None
    __state = GameState.STARTED

    def __init__(self):
        self.__players = PlayerCollection()

    def new_player(self):
        if len(self.__players) == MAX_PLAYERS:
            raise MaxPlayersExceededException()
        player = PlayerFactory.create()
        self.__players.add(player)
        self.__state = GameState.TWO_PLAYERS_READY if self.__state == GameState.ONE_PLAYER_READY else GameState.ONE_PLAYER_READY
        return player
    
    def new_level(self):
        self.__level = LevelFactory.create()
        self.__level.load_map().create()
        self.__level.load_bots()
        for player in self.__players:
            player.add_tank(self.__level.map.player_tanks[player.char])
            player.tank.symbol = str(player.number)
            self.__level.map.add_object(player.tank)
        return self.__level
    
    def play_level(self):
        if self.__state not in [GameState.TWO_PLAYERS_READY, GameState.ONE_PLAYER_READY]:
            raise Exception("There is not players ready to play.")
        self.__state = GameState.ONE_PLAYER_PLAYING if self.__state == GameState.ONE_PLAYER_READY else GameState.TWO_PLAYERS_PLAYING
    
    @property
    def level(self):
        if self.__level is None:
            raise LevelDoesNotExistsException()
        return self.__level
    
    @property
    def players(self):
        return self.__players
    
    def __str__(self):
        return TO_STRING % (self.__players, self.__level.number, self.__level.map, self.__level.bots)