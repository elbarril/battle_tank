from models.game.player.Player import Player
from models.game.player.PlayerMovements import PlayerMovements
from utils.Factory import Factory
from exceptions.game import *
from constants.game import *

class PlayerFactory(Factory):
    @classmethod
    def number(cls):
        return cls._number(Player)

    @classmethod
    def create(cls):
        player:Player = cls._create(Player)
        player.number = cls._number(Player)
        player.movements = PlayerMovements.get(player.number)
        return player