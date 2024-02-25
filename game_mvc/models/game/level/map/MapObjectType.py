from enum import Enum

class MapObjectType(Enum):
    FLUID = "0"
    SOLID = "1"
    PLAYER_ONE = "O"
    PLAYER_TWO = "T"
    BOT_TANK = "B"