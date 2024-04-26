from ..map.object import MapObject
from ..map.object.MapObjectType import MapObjectType

from ..map.object.passable import Forest
from ..map.object.passable import Gravel
from ..map.object.passable import Lake

from ..map.object.solid import Wall
from ..map.object.solid import Block
from ..map.object.solid import Eagle

from ..map.object.tank import BotTank
from ..map.object.tank import PlayerOneTank, PlayerTwoTank, PlayerTank


STATIC_OBJECT_TYPES:dict[MapObjectType, type[MapObject]] = {
    MapObjectType.WALL: Wall,
    MapObjectType.IRON: Block,
    MapObjectType.EAGLE: Eagle,
    MapObjectType.FOREST: Forest,
    MapObjectType.GRAVEL: Gravel,
    MapObjectType.LAKE: Lake
}

BOT_TANK_TYPES:dict[MapObjectType, type[BotTank]] = {
    MapObjectType.BOT_TANK: BotTank
}

PLAYER_TANK_TYPES:dict[MapObjectType, type[PlayerTank]] = {
    MapObjectType.PLAYER_ONE: PlayerOneTank,
    MapObjectType.PLAYER_TWO: PlayerTwoTank
}

class MapObjectCreator:
    @classmethod
    def create(cls, *args):
        pass

    @classmethod
    def all(cls):
        pass

class BotTankCreator(MapObjectCreator):
    __bot_tanks:set[BotTank] = set()
    
    @classmethod
    def create(cls, tank_type, position, size):
        bot_tank = BOT_TANK_TYPES[tank_type](position, size)
        cls.__bot_tanks.add(bot_tank)
        return bot_tank

    @classmethod
    def all(cls):
        return cls.__bot_tanks

class PlayerTankCreator(MapObjectCreator):
    __player_tanks:set[PlayerTank] = set()
    
    @classmethod
    def create(cls, tank_type, position, size):
        player_tank = PLAYER_TANK_TYPES[tank_type](position, size)
        cls.__player_tanks.add(player_tank)
        return player_tank

    @classmethod
    def all(cls):
        return cls.__player_tanks

    
class StaticObjectCreator(MapObjectCreator):
    __statics:set[MapObject] = set()
    
    @classmethod
    def create(cls, type, position, size):
        static = STATIC_OBJECT_TYPES[type](position, size)
        cls.__statics.add(static)
        return static

    @classmethod
    def all(cls):
        return cls.__statics

class MapObjectFactory:
    def _create_map_object(self, object_type, position, size):
        if object_type in BOT_TANK_TYPES: 
            return BotTankCreator.create(object_type, position, size)
        elif object_type in PLAYER_TANK_TYPES: 
            return PlayerTankCreator.create(object_type, position, size)
        elif object_type in STATIC_OBJECT_TYPES: 
            return StaticObjectCreator.create(object_type, position, size)

    @property
    def statics(self):
        return StaticObjectCreator.all()

    @property
    def player_tanks(self):
        return PlayerTankCreator.all()

    @property
    def bot_tanks(self):
        return BotTankCreator.all()