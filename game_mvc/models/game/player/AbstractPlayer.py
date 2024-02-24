from abc import ABC, abstractmethod
from models.game.player.Tank import Tank

class AbstractPlayer(ABC):
    tank = None
    number = None
    is_bot = None
    movements = None

    @abstractmethod
    def add_tank(self, tank:Tank):
        if not isinstance(tank, Tank):
            raise Exception()
        self.tank = tank