from enum import Enum

class MapObjectType(Enum):
    FLUID = "0"
    SOLID = "1"
    PLAYER_ONE = "O"
    PLAYER_TWO = "T"
    BOT_TANK = "B"

    def __init__(self, object_char:str):
        if not isinstance(object_char, str):
            raise Exception()
        super().__init__(object_char)