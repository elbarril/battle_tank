from abc import ABC, abstractmethod
from models.game.player.Tank import Tank

class AbstractPlayer(ABC):
    is_bot = None
    movements = None

    def __init__(self, number=None, tank=None):
        self.number = number
        self.tank = tank

    @abstractmethod
    def add_tank(self, tank:Tank):
        if not isinstance(tank, Tank):
            return Exception(f"Cannot add {type(tank)} object as a tank.")
        if self.tank:
            return Exception(f"Player {self} already has a tank.")
        self.tank = tank