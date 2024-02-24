from abc import ABC, abstractmethod
from models.game.player.Tank import Tank

class AbstractPlayer(ABC):
    number = None
    is_bot = None
    movements = None

    def __init__(self, tank=None):
        self.tank = tank

    @abstractmethod
    def add_tank(self, tank:Tank):
        if not isinstance(tank, Tank):
            raise Exception()
        if self.tank:
            raise Exception(f"Player {self} already has a tank.")
        self.tank = tank