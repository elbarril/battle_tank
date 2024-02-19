from models.game.level.map.MapObject import MapObject
from models.game.level.map.objects.FluidMapObject import FluidMapObject
from models.game.level.map.objects.SolidMapObject import SolidMapObject
from models.game.player.Tank import Tank
from models.game.player.BotTank import BotTank

from utils.Factory import Factory

class NotMappedMapObjectTypeException(Exception):
    def __init__(self, *args):
        super().__init__("Not mapped map object char.", *args)

class MapObjectFactory(Factory):
    __map_objects = {
        "0": FluidMapObject,
        "1": SolidMapObject,
        "O": Tank,
        "T": FluidMapObject,
        "B": BotTank
    }

    @classmethod
    def create(cls, object_char, position) -> MapObject:
        if not object_char in cls.__map_objects:
            raise NotMappedMapObjectTypeException()
        object_type = cls.__map_objects.get(object_char)
        if object_type:
            return cls._create(object_type, position)