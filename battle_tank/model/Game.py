from model.Map import Map
from model.Bot import Bot, Player
from model.Level import Level
from constants import (
    MAP_HEIGHT,
    MAP_WIDTH,
    FIRST_LEVEL
)

class Game:
    def __init__(self):
        super().__init__()
        self.__map = Map(width=MAP_WIDTH, height=MAP_HEIGHT)
        self.__level:Level = None
        self.__players:list[Player] = []
        self.__bot = Bot(self)

    @property
    def map(self): return self.__map

    @property
    def bot(self): return self.__bot

    @property
    def players(self): return self.__players

    @property
    def level(self): return self.__level

    def load(self, level_id:int=FIRST_LEVEL):
        self.__level = Level(level_id)
        
        for tank in self.__level.player_tanks:
            player = Player()
            player.tank = tank
            self.__players.append(player)

        for tank in self.__level.bot_tanks:
             self.__bot.add_tank(tank)

        return self