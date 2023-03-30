from model.game.Entity import Entity
from model.game.board.Position import Position

class Movable(Entity):
    def __init__(self, position:Position,  direction:str, speed:int):
        super().__init__(position=position, is_solid=True)
        self.__direction:str = direction
        self.__speed:int = speed
    
    def move(self) -> None:
        self.position = self.next_position

    @property
    def direction(self) -> str:
        return self.__direction
    
    @direction.setter
    def direction(self, direction:str) -> None:
        self.__direction:str = direction

    @property
    def speed(self) -> int:
        return self.__speed
    
    @speed.setter
    def speed(self, speed:int) -> None:
        self.__speed:int = speed
    
    @property
    def next_position(self) -> Position:
        next_row = self.next_row
        next_column = self.next_column
        return Position(next_row, next_column)

    @property
    def next_column(self) -> int:
        from model.Constants import DIRECTION_LEFT, DIRECTION_RIGHT
        next_column:int = (self.position.column + self.speed) if self.direction == DIRECTION_RIGHT else (self.position.column - self.speed) if self.direction == DIRECTION_LEFT else self.position.column
        return next_column
    
    @property
    def next_row(self) -> int:
        from model.Constants import DIRECTION_UP, DIRECTION_DOWN
        next_row = (self.position.row + self.speed) if self.direction == DIRECTION_DOWN else (self.position.row - self.speed) if self.direction == DIRECTION_UP else self.position.row
        return next_row
    
    def __repr__(self):
        return super().__repr__()