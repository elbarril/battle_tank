from models.game.level.map.MapObject import MapObject
from models.game.level.map.MapObjectChar import MapObjectChar

from models.game.level.map.objects.FluidMapObject import FluidMapObject
from models.game.level.map.objects.SolidMapObject import SolidMapObject

from models.game.player.PlayerTank import PlayerTank
from models.game.player.BotTank import BotTank

from utils.Factory import Factory

class NotMappedMapObjectTypeException(Exception):
    def __init__(self, *args):
        super().__init__("Not mapped map object char.", *args)


class MapObjectFactory(Factory):
    __map_objects = {
        MapObjectChar.FLUID.value: FluidMapObject,
        MapObjectChar.SOLID.value: SolidMapObject,
        MapObjectChar.PLAYER_ONE.value: PlayerTank,
        MapObjectChar.PLAYER_TWO.value: PlayerTank,
        MapObjectChar.BOT_TANK.value: BotTank
    }

    @classmethod
    def create(cls, object_char, *args, **kwargs) -> MapObject:
        if not object_char in cls.__map_objects:
            raise NotMappedMapObjectTypeException()
        object_type = cls.__map_objects.get(object_char)
        if object_type:
            return cls._create(object_type, *args, **kwargs)