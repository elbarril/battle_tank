from constants.map import MAP_WIDTH, MAP_HEIGHT

class MapSize:
    def __init__(self, width=MAP_WIDTH, height=MAP_HEIGHT):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height