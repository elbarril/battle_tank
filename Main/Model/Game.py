from Main.Model.Tank import Tank
from Main.Model.Board import Board
from Main.Model.LevelFactory import LevelFactory
from Main.Model.Constants import GAME_TITLE, PLAYER_SPAWN_COLUMN, PLAYER_SPAWN_ROW, PLAYER_SPAWN_DIRECTION, PLAYER_SPAWN_SPEED
from pygame.time import Clock
from pygame import time

class Game:
    __title:str = GAME_TITLE
    __instance = None
    __board:Board = None
    __level_factory:LevelFactory = None
    __player_tank:Tank = None
    __clock:Clock = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.initialize()
        return cls.__instance

    @classmethod
    def initialize(cls):
        cls.__instance = cls()
        cls.__board = Board.get_instance()
        cls.__level_factory = LevelFactory.get_instance()
        cls.__player_tank = Tank(column=PLAYER_SPAWN_COLUMN, row=PLAYER_SPAWN_ROW, direction=PLAYER_SPAWN_DIRECTION, speed=PLAYER_SPAWN_SPEED)
        cls.__clock = Clock()

    @property
    def clock(self) -> Clock:
        return self.__clock

    @property
    def time(self) -> int:
        return int(time.get_ticks() / 1000)

    @property
    def title(self) -> str:
        return self.__title

    @property
    def player_tank(self) -> Tank:
        return self.__player_tank

    @property
    def board(self) -> Board:
        return self.__board

    @property
    def level_factory(self) -> LevelFactory:
        return self.__level_factory
    
    def start(self) -> None:
        self.clock.tick(60)
        if self.board.positions is None:
            raise Exception("Board hasn't positions.")
        self.board.add_level_elements(self.level_factory.first_level.elements)
        self.board.add_tank(self.player_tank)
    
    def load_next_level(self) -> None:
        self.board.add_level_elements(self.level_factory.get_next_level().elements)
        self.board.add_tank(self.player_tank)

    def update(self) -> None:
        self.board.remove_previous_tank(self.player_tank)
        self.board.add_tank(self.player_tank)
        for bullet in self.board.bullets:
            self.board.remove_previous_bullet(bullet)
            self.board.add_bullet(bullet)