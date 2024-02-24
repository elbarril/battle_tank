from utils.Factory import Factory
from models.game.player.Player import Player
from models.game.player.PlayerMovements import PlayerMovements
from models.game.level.map.MapObjectType import MapObjectType

class PlayerFactory(Factory):
    __player_tank_type = {
        1: MapObjectType.PLAYER_ONE,
        2: MapObjectType.PLAYER_TWO
    }

    @classmethod
    def create(cls):
        player:Player = cls._create(Player)
        player.number = cls._number(Player)
        player.movements = PlayerMovements.get(player.number)
        player.type = cls.__player_tank_type[player.number]
        return player