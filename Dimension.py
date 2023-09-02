from Position import POSITION_WIDTH, POSITION_HEIGHT

class Dimension:
    def __init__(self, rows:int, columns:int):
        self.__rows = rows
        self.__columns = columns
        self.__width = rows * POSITION_WIDTH
        self.__height = columns * POSITION_HEIGHT
        
    @property
    def width(self) -> int:
        return self.__width
        
    @property
    def columns(self) -> int:
        return self.__columns
        
    @property
    def height(self) -> int:
        return self.__height
        
    @property
    def rows(self) -> int:
        return self.__rows
        
    @width.setter
    def width(self, width:int) -> int:
        self.__width = width
        
    @height.setter
    def height(self, height:int) -> int:
        self.__height = height