class Square:
    def __init__(self, side:int):
        self.__side = side

    @property
    def radio(self): return self.__side / 2

    @property
    def side(self): return self.__side