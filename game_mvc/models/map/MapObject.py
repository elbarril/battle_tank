from abc import ABC

from models.map.MapObjectPosition import MapObjectPosition
from models.map.MapObjectSize import MapObjectSize

from constants.text import TO_STRING_OBJECT

class MapObject(ABC):
    __is_solid = None
    __symbol = None

    def __init__(self, position:MapObjectPosition, size=MapObjectSize(1,1)):
        self.__position = position
        self.__size = size
    
    @property
    def is_solid(self):
        return self.__is_solid
    
    @is_solid.setter
    def is_solid(self, is_solid):
        self.__is_solid = is_solid

    @property
    def symbol(self):
        return self.__symbol
    
    @symbol.setter
    def symbol(self, symbol):
        self.__symbol = symbol

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size):
        self.__size = size

    def __str__(self):
        return TO_STRING_OBJECT
    