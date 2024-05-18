from abc import abstractmethod

from ..abstract.SolidMapObject import SolidMapObject
from ..abstract.MovableMapObject import MovableMapObject


class Tank(MovableMapObject, SolidMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.symbol = "T"
        self.shooting = False

    @abstractmethod
    def shoot(self):
        pass
