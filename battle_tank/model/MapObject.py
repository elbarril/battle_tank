from model.Square import Square
from model.Position import Position
from abc import ABC, abstractmethod

class MapObject(Square, ABC):
    def __init__(self, position:Position, side:int):
        super().__init__(side)
        self.__id:int = None
        self.__code:int = None
        self.__position = position

    @property
    def id(self): return self.__id

    @id.setter
    def id(self, id:int): self.__id = id

    @property
    def position(self): return self.__position

    @position.setter
    def position(self, position:Position): self.__position = position

    @property
    def code(self): return self.__code

    @code.setter
    def code(self, code:int): self.__code = code

    @property
    @abstractmethod
    def list(self): return [self]