from models.game.map.MapObject import MapObject
from models.game.map.MapObjectType import MapObjectType
from models.game.map.MapObjectPosition import MapObjectPosition

from models.game.map.objects.FluidMapObject import FluidMapObject
from models.game.map.objects.SolidMapObject import SolidMapObject
from models.game.map.objects.PlayerTank import PlayerTank
from models.game.map.objects.BotTank import BotTank

from utils.Factory import Factory


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
        if object_type in cls.__map_object_classes:
            object_class = cls.__map_object_classes.get(object_type)
            position = MapObjectPosition(x, y)
            return cls._create(object_class, position)