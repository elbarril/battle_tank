from models.map.MapObject import MapObject
from models.map.MapObjectType import MapObjectType
from models.map.MapPosition import MapPosition
from models.map.MapObjectPosition import MapObjectPosition
from models.map.MapObjectSize import MapObjectSize

from models.map.objects.FluidMapObject import FluidMapObject
from models.map.objects.BrickCompound import BrickCompound
from models.map.objects.PlayerTank import PlayerTank
from models.map.objects.BotTank import BotTank

from utils.Factory import Factory
from constants.map import MAP_POSITION_WIDTH, MAP_POSITION_HEIGHT

class MapObjectFactory(Factory):
    __map_object_classes = {
        MapObjectType.FLUID: FluidMapObject,
        MapObjectType.BRICK: BrickCompound,
        MapObjectType.PLAYER_ONE: PlayerTank,
        MapObjectType.PLAYER_TWO: PlayerTank,
        MapObjectType.BOT_TANK: BotTank
    }

    @classmethod
    def create(cls, object_type, x, y, size=MapObjectSize(MAP_POSITION_WIDTH,MAP_POSITION_HEIGHT)) -> MapObject:
        if object_type in cls.__map_object_classes:
            object_class = cls.__map_object_classes.get(object_type)
            position = MapPosition(x, y)
            return cls._create(object_class, position, size)
        
    @classmethod
    def create_empty(cls, x, y, size):
        size = size or MapObjectSize(MAP_POSITION_WIDTH,MAP_POSITION_HEIGHT)
        return cls.create(MapObjectType.FLUID, x, y, size)