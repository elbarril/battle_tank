from MapObject import MapObject

class Brick(MapObject):
    __width = __height = 1
    __image_file = 'brick.png'
    def __init__(self, row:int, column:int):
        super().__init__(row, column, self.__width, self.__height, self.__image_file)