from Main.Model.Static import Static
from abc import ABC


class Destroyable(Static, ABC):

    __resistance = 1

    def getResistance(self):
        return self.__resistance

