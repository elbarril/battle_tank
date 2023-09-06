from Constants import DIRECTIONS

class Direction:
    def __init__(self, key:str):
        self.__key = key
        if DIRECTIONS.get(key) is None:
            raise Exception()
        self.__row, self.__column, self.__suffix = DIRECTIONS[key]
    
    @property
    def key(self):
        return self.__key
    
    @property
    def row(self):
        return self.__row
    
    @property
    def column(self):
        return self.__column
    
    @property
    def suffix(self):
        return self.__suffix
    
    def __eq__(self, direction):
        return isinstance(direction, Direction) and self.key == direction.key
    
    def __ne__(self, direction):
        return not self.__eq__(direction)