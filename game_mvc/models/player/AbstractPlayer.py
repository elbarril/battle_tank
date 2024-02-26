from abc import ABC, abstractmethod

from models.map.objects.Tank import Tank

class AbstractPlayer(ABC):
    is_bot = None
    movements = None

    def __init__(self, number=None, tank=None):
        self.number = number
        self.tank = tank

    @abstractmethod
    def add_tank(self, tank:Tank):
        self.tank = tank