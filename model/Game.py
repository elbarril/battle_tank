from controller.PyGame import PyGame

from model.game.Direction import Direction
from model.game.Keyboard import Keyboard
from model.game.level.Level import Level
from model.game.entity.Movable import Movable
from model.game.LevelFactory import LevelFactory
from model.game.Player import Player
from model.game.CollisionManager import CollisionManager


class Game(PyGame):
    __instance = None
    __player:Player = None
    __level:Level = None

    def __init__(self):
        super().__init__()

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.initialize()
        return cls.__instance

    @classmethod
    def initialize(cls):
        cls.__level_factory:LevelFactory = LevelFactory.get_instance()
        cls.__instance = cls()

    @property
    def title(self) -> str:
        from model.Constants import GAME_TITLE
        return GAME_TITLE

    @property
    def level(self) -> Level:
        return self.__level

    @level.setter
    def level(self, level:Level) -> None:
        self.__level = level

    @property
    def player(self) -> Player:
        return self.__player

    @player.setter
    def player(self, player:Player) -> None:
        self.__player = player

    @property
    def level_factory(self) -> LevelFactory:
        return self.__level_factory

    def play_level(self) -> None:
        self.clock.tick(60)
        self.player_event_actions()
        self.level.play_bullets()
    
    def load_next_level(self) -> None:
        self.player = Player()
        self.level = self.level_factory.next_level
        self.level.board.add_entity(self.player.tank)

    def player_event_actions(self):
        for event in self.player.events:
            if event.is_key_pressed:
                if Keyboard.is_direction_key(event.key):
                    self.player.tank.direction = Direction.get(event.key)
                    if self.level.board.is_valid_position(self.player.tank.next_position):
                        self.level.board.remove_entity(self.player.tank)
                        collided_entity = CollisionManager.hits(self.level.board.get_square(self.player.tank.next_position))
                        if not collided_entity:
                            self.player.tank.move()
                        elif isinstance(collided_entity, Movable):
                            self.player.remove_life()
                            self.player.respawn()
                        self.level.board.add_entity(self.player.tank)
                if Keyboard.is_shoot_key(event.key):
                    bullet = self.player.tank.shoot()
                    self.level.board.add_entity(bullet)
            if event.is_quit:
                self.quit()