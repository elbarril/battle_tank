from Tank import Tank
from Constants import PLAYER_TANK_IMAGE_FILENAME, MAP_OBJECT_MAX_SIZE

class Player:
    def __init__(self, row:int, column:int):
        self.__tank = Tank(row, column, MAP_OBJECT_MAX_SIZE, PLAYER_TANK_IMAGE_FILENAME)

    @property
    def tank(self) -> Tank:
        return self.__tank