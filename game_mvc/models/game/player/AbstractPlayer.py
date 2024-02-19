from abc import ABC, abstractmethod

class AbstractPlayer(ABC):
    tank = None
    number = ''
    is_bot = None
    movements = None

    @abstractmethod
    def add_tank(self):
        pass