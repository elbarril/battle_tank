class Dimension:
    def __init__(self, width:int, height:int):
        self.__width = width
        self.__height = height
        
    @property
    def width(self) -> int:
        return self.__width
        
    @property
    def height(self) -> int:
        return self.__height
        
    @width.setter
    def width(self, width:int) -> int:
        self.__width = width
        
    @height.setter
    def height(self, height:int) -> int:
        self.__height = height