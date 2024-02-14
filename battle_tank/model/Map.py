class Map:
    def __init__(self, width:int, height:int):
        self.__width = width
        self.__height = height

    @property
    def width(self): return self.__width

    @property
    def height(self): return self.__height

    def is_out_of_limits(self, area:tuple[int,int,int,int]) -> bool:
        left, top, right, bottom = area
        return  left < 0 or top < 0 or right > self.width or bottom > self.height