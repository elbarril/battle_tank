POSITION_WIDTH = POSITION_HEIGHT = 10

class Position:
    def __init__(self, row:int, column:int):
        self.__row = row
        self.__column = column
        
    @property
    def row(self) -> int:
        return self.__row
    
    @property
    def column(self) -> int:
        return self.__column
    
    @property
    def x(self) -> int:
        return self.column * POSITION_WIDTH
    
    @property
    def y(self) -> int:
        return self.row * POSITION_HEIGHT
    
    def __repr__(self) -> str:
        return f"({self.row},{self.column})"
    