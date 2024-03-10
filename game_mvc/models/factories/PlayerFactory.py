from utils.Factory import Factory
from models.player.Player import Player
from models.player.PlayerMovements import PlayerMovements
from models.player.PlayerShoot import PlayerShoot

class PlayerFactory(Factory):
    @classmethod
    def create(cls, player_number):
        player:Player = cls._create(Player, player_number)
        player.movements = PlayerMovements.get(player_number)
        player.shoot = PlayerShoot.get(player_number)
        return player