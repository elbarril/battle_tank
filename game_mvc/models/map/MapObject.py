from abc import ABC

from models.map.MapPosition import MapPosition
from models.map.MapObjectSize import MapObjectSize

class MapObject(ABC):
    __symbol = None
    __color = None
    _image = None

    def __init__(self, position:MapPosition, size:MapObjectSize):
        if not isinstance(position, MapPosition):
            raise TypeError(f"Wrong position type: {position}")
        if not isinstance(size, MapObjectSize):
            raise TypeError(f"Wrong size type: {size}")
        self.__position = position
        self.__size = size
    
    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, image):
        self._image = image

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
        if not isinstance(position, MapPosition):
            raise TypeError(f"Wrong position type: {position}")
        self.__position = position

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size):
        self.__size = size
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

    def __repr__(self):
        return type(self).__name__