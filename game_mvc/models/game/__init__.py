from models.game.GameStateManager import GameStateManager
from models.game.GameModeManager import GameMode, GameModeManager

from models.level import Level
from models.player import HumanPlayer, PlayerOne, PlayerTwo

class LevelFactory:
    
    @classmethod
    def set_config(cls, config:dict):
        cls.__max = config.get("max")
        cls.__first = config.get("first")
        cls.__map = config.get("map")
        cls.__files = config.get("files")

    @classmethod
    def next_level(cls, current:Level=None):
        if current.number and current.number + 1 <= cls.__max:
            return Level(current.number + 1, cls.__map)
        else: return Level(cls.__first, cls.__map)

from config import CONFIG

class Singleton:
    """One single instance abstract class."""
    __instances = {}
    def __new__(cls):
        if cls.__instances.get(cls) is None:
            instance = super().__new__(cls)
            cls.__instances.setdefault(cls, instance)
        return cls.__instances.get(cls)

class Game(Singleton):
    """Main game model."""
    def __init__(self, config=CONFIG):
        """Game init.
        
        Parameters
        ----------
        config : dict
            players, levels and map configuration
            example:
                CONFIG = {
                    "levels": {
                        "first": 1,
                        "max": 99,
                        "files": {
                            "prefix": "level_",
                            "path": "./maps/",
                            "extension": ".csv"
                        }
                    },
                    "maps":{
                        "rows": 20,
                        "columns": 20
                    },
                    "players": [1, 2],
                    "ppp": 10
                }
        """
        self.__mode_manager = GameModeManager()
        self.__state_manager = GameStateManager()

        self.__players:dict[int, HumanPlayer] = {}
        self.__level:Level = LevelFactory()
    
    def reset(self):
        """To reset game as instance init."""
        self.__mode_manager.set_one_player()
        self.__state_manager.game_init()
        self.__players:dict[int, HumanPlayer] = {}
        self.__level:Level = None

    def toggle_players_mode(self):
        """To switch players mode. One to two or two to one."""
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
    def mode(self):
        """Players mode"""
        return self.__mode_manager.mode
    
    @property
    def level(self):
        """Game current level."""
        return self.__level
    
    @property
    def players(self):
        """Game available players."""
        return [player for player in self.__players.values() if player is not None]