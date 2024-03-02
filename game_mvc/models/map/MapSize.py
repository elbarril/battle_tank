from constants.map import MAP_WIDTH, MAP_HEIGHT, MAP_POSITION_WIDTH, MAP_POSITION_HEIGHT

class MapSize:
    def __init__(self, width=MAP_WIDTH*MAP_POSITION_WIDTH, height=MAP_HEIGHT*MAP_POSITION_HEIGHT):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
    
    def __str__(self):
        return str(self.width) + str(self.height)