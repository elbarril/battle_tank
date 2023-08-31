from Tank import Tank

class Player:
    __width = __height = 1
    __image_url = 'playertank.png'
    def __init__(self, row:int, column:int):
        self.__tank = Tank(row, column, self.__width, self.__height, self.__image_url)

    @property
    def tank(self) -> Tank:
        return self.__tank