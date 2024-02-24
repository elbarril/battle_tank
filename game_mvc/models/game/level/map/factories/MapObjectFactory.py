from models.game.level.map.MapObject import MapObject
from models.game.level.map.MapObjectType import MapObjectType
from models.game.level.map.MapObjectPosition import MapObjectPosition

from models.game.level.map.objects.FluidMapObject import FluidMapObject
from models.game.level.map.objects.SolidMapObject import SolidMapObject

from models.game.player.PlayerTank import PlayerTank
from models.game.player.BotTank import BotTank

from utils.Factory import Factory

class NotMappedMapObjectTypeException(Exception):
    def __init__(self, *args):
        super().__init__("Not mapped map object char.", *args)


class MapObjectFactory(Factory):
    __map_object_classes = {
        MapObjectType.FLUID: FluidMapObject,
        MapObjectType.SOLID: SolidMapObject,
        MapObjectType.PLAYER_ONE: PlayerTank,
        MapObjectType.PLAYER_TWO: PlayerTank,
        MapObjectType.BOT_TANK: BotTank
    }

    @classmethod
    def create(cls, object_type, x, y) -> MapObject:
        if not object_type in cls.__map_object_classes:
            raise NotMappedMapObjectTypeException()
        object_class = cls.__map_object_classes.get(object_type)
        if object_class:
            position = MapObjectPosition(x, y)
            return cls._create(object_class, position)
        
    @classmethod
    def create_empty(cls, position):
        object_class = cls.__map_object_classes.get(MapObjectType.FLUID.value)
        return cls._create(object_class, position)