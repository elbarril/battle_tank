from enum import Enum

from . import MapObject
from .solid import Wall
from .solid import Block
from .solid import Eagle
from .tank import BotTank
from .passable import Lake
from .passable import Forest
from .passable import Gravel
from .tank import PlayerOneTank, PlayerTwoTank


class MapObjectTypeCode(Enum):
    NONE = "0"
    WALL = "W"
    PLAYER_ONE = "O"
    PLAYER_TWO = "T"
    BOT_TANK = "B"
    GRAVEL = "G"
    FOREST = "F"
    IRON = "I"
    EAGLE = "E"
    LAKE = "L"


PLAYER_TANK_TYPES = [
    MapObjectTypeCode.PLAYER_ONE,
    MapObjectTypeCode.PLAYER_TWO
]

BOT_TANK_TYPES = [
    MapObjectTypeCode.BOT_TANK
]

STATIC_TYPES = [
    MapObjectTypeCode.WALL,
    MapObjectTypeCode.IRON,
    MapObjectTypeCode.EAGLE,
    MapObjectTypeCode.FOREST,
    MapObjectTypeCode.GRAVEL,
    MapObjectTypeCode.LAKE
]

MAP_OBJECT_TYPES: dict[MapObjectTypeCode, type[MapObject]] = {
    MapObjectTypeCode.NONE: None,
    MapObjectTypeCode.WALL: Wall,
    MapObjectTypeCode.IRON: Block,
    MapObjectTypeCode.EAGLE: Eagle,
    MapObjectTypeCode.FOREST: Forest,
    MapObjectTypeCode.GRAVEL: Gravel,
    MapObjectTypeCode.LAKE: Lake,
    MapObjectTypeCode.BOT_TANK: BotTank,
    MapObjectTypeCode.PLAYER_ONE: PlayerOneTank,
    MapObjectTypeCode.PLAYER_TWO: PlayerTwoTank
}
