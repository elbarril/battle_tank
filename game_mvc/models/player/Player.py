from models.map.MovableObjectDirection import MovableObjectDirections

from constants.text import TO_STRING_PLAYER
from constants.game import FIRST_PLAYER, SECOND_PLAYER

class Player:
    def __init__(self, number):
        self.number = number
        self.tank = None
        self.movements = None
        self.shoot = None

    def add_tank(self, tank):
        self.tank = tank

    def __str__(self):
        return TO_STRING_PLAYER % self.number

class PlayerOne(Player):
    def __init__(self):
        super().__init__(FIRST_PLAYER)
        self.movements = (
            ("up", MovableObjectDirections.UP),
            ("down", MovableObjectDirections.DOWN),
            ("left", MovableObjectDirections.LEFT),
            ("right", MovableObjectDirections.RIGHT),
        )
        self.shoot = ("m",)

class PlayerTwo(Player):
    def __init__(self):
        super().__init__(SECOND_PLAYER)
        self.movements = (
            ("w", MovableObjectDirections.UP),
            ("s", MovableObjectDirections.DOWN),
            ("a", MovableObjectDirections.LEFT),
            ("d", MovableObjectDirections.RIGHT),
        )
        self.shoot = ("space",)