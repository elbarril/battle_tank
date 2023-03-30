from controller.PyGame import PyGame

from model.game.Direction import Direction
from model.game.Keyboard import Keyboard
from model.game.Board import Board
from model.game.entity.Movable import Movable
from model.game.Bot import Bot
from model.game.LevelFactory import LevelFactory
from model.game.Player import Player
from model.game.CollisionManager import CollisionManager
from model.game.entity.movable.Bullet import Bullet
from model.game.entity.movable.Tank import Tank


class Game(PyGame):
    __instance = None

    def __init__(self):
        super().__init__()

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.initialize()
        return cls.__instance

    @classmethod
    def initialize(cls):
        cls.__board:Board = Board.get_instance()
        cls.__level_factory:LevelFactory = LevelFactory.get_instance()
        cls.__player:Player = Player()
        cls.__bullets:list[Bullet] = []
        cls.__bots:list[Bot] = []

        cls.__instance = cls()

    @property
    def title(self) -> str:
        from model.Constants import GAME_TITLE
        return GAME_TITLE

    @property
    def player(self) -> Player:
        return self.__player

    @property
    def board(self) -> Board:
        return self.__board

    @property
    def level_factory(self) -> LevelFactory:
        return self.__level_factory
    
    @property
    def bullets(self) -> list[Bullet]:
        return self.__bullets
    
    @property
    def bots(self) -> list[Bot]:
        return self.__bots
    
    @property
    def has_bullets(self) -> bool:
        return True if len(self.bullets) else False
    
    @property
    def has_bots(self) -> bool:
        return True if len(self.bots) else False

    def play_level(self) -> None:
        self.clock.tick(60)
        self.player_event_actions()
        if self.has_bullets:
            for bullet in self.bullets:
                self.move_entity(bullet)
    
    def load_next_level(self) -> None:
        self.__current_level = self.level_factory.next_level
        for static in self.__current_level.statics:
            self.board.add_entity(static)
        for bot in self.__current_level.bots:
            self.board.add_entity(bot.tank)
            self.bots.append(bot)
        self.board.add_entity(self.player.tank)

    def player_event_actions(self):
        for event in self.player.events:
            if event.is_key_pressed:
                if Keyboard.is_direction_key(event.key):
                    self.player.tank.direction = Direction().get(event.key)
                    self.move_entity(self.player.tank)
                if Keyboard.is_shoot_key(event.key):
                    bullet = self.player.tank.shoot()
                    self.bullets.append(bullet)
            if event.is_quit:
                self.quit()

    # FIXME
    def move_entity(self, entity:Movable) -> None:
        if self.board.is_valid_position(entity.next_position):
            collided_entity = CollisionManager.hits(self.board.get_square(entity.next_position))
            if not collided_entity:
                self.board.remove_entity(entity)
                entity.move()
                self.board.add_entity(entity)
            elif collided_entity and isinstance(entity, Bullet):
                self.board.remove_entity(entity)
            elif isinstance(collided_entity, Movable) and entity is self.player.tank:
                self.player.lifes -= 1
        elif isinstance(entity, Bullet):
            self.board.remove_entity(entity)
