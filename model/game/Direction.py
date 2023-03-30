from pygame import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)
from model.Constants import (
    DIRECTION_UP,
    DIRECTION_DOWN,
    DIRECTION_LEFT,
    DIRECTION_RIGHT
)

class Direction:
    def __init__(self):
        self.__directions = {
            K_UP: DIRECTION_UP,
            K_DOWN: DIRECTION_DOWN,
            K_LEFT: DIRECTION_LEFT,
            K_RIGHT: DIRECTION_RIGHT
        }

    def get(self, key):
        return self.__directions[key]