from models.map.MapObject import MapObject
from models.map.MapObjectType import MapObjectType
from models.map.MapPosition import MapPosition

from models.map.objects.FluidMapObject import FluidMapObject
from models.map.objects.SolidMapObject import SolidMapObject
from models.map.objects.PlayerTank import PlayerTank
from models.map.objects.BotTank import BotTank

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
            position = MapPosition(x, y)
            return cls._create(object_class, position)