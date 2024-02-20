from utils.Factory import Factory
from models.game.player.Player import Player
from models.game.player.PlayerMovements import PlayerMovements
from models.game.level.map.MapObjectChar import MapObjectChar

class PlayerFactory(Factory):
    __player_tank_char = {
        1: MapObjectChar.PLAYER_ONE.value,
        2: MapObjectChar.PLAYER_TWO.value
    }

    @classmethod
    def create(cls):
        player:Player = cls._create(Player)
        player.number = cls._number(Player)
        player.movements = PlayerMovements.get(player.number)
        player.char = cls.__player_tank_char[player.number]
        return player