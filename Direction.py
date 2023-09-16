class Direction:
    def __init__(self, values:tuple[int|str]):
        self.__row, self.__column, self.__suffix = values
    
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
        return isinstance(direction, Direction) and self.row == direction.row and self.column == direction.column
    
    def __ne__(self, direction):
        return not self.__eq__(direction)