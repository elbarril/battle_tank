from model.Tank import Tank
from constants import PLAYER_MAP_CODE

class Player:
    def __init__(self):
        self.__tank = None

    @property
    def tank(self) -> Tank:
        return self.__tank

    @tank.setter
    def tank(self, tank:Tank) -> None:
        tank.code = PLAYER_MAP_CODE
        self.__tank = tank