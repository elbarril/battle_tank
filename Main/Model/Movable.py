from Main.Model.MapElement import MapElement
from typing import Literal
from Main.Model.Constants import UNSET_POSITION

class Movable(MapElement):
    def __init__(self, column:int, row:int,  direction:Literal["up", "down", "left", "right"], speed:int):
        self.__column:int = column
        self.__row:int = row
        self.__direction:Literal["up", "down", "left", "right"] = direction
        self.__speed:int = speed
        self.__is_solid:bool = True
        self.__previous_row, self.__previous_column = UNSET_POSITION
    
    def move(self) -> None:
        self.previous_column = self.column
        self.previous_row = self.row
        if self.direction == "up":
            self.row -= self.speed
        elif self.direction == "down":
            self.row += self.speed
        elif self.direction == "left":
            self.column -= self.speed
        elif self.direction == "right":
            self.column += self.speed

    @property
    def direction(self) -> Literal["up", "down", "left", "right"]:
        return self.__direction
    
    @direction.setter
    def direction(self, direction:Literal["up", "down", "left", "right"]) -> None:
        self.__direction:Literal["up", "down", "left", "right"] = direction

    @property
    def speed(self) -> int:
        return self.__speed
    
    @speed.setter
    def speed(self, speed:int) -> None:
        self.__speed:int = speed

    @property
    def column(self) -> int:
        return self.__column
        
    @column.setter
    def column(self, column:int) -> None:
        self.__column:int = column
    
    @property
    def previous_column(self) -> int:
        return self.__previous_column

    @previous_column.setter
    def previous_column(self, previous_column:int) -> None:
        self.__previous_column = previous_column

    @property
    def next_column(self) -> int:
        return (self.__column + self.speed) if self.direction == "right" else (self.__column - self.speed) if self.direction == "left" else self.__column

    @property
    def row(self) -> int:
        return self.__row
        
    @row.setter
    def row(self, row:int) -> None:
        self.__row:int = row
    
    @property
    def previous_row(self) -> int:
        return self.__previous_row
    
    @previous_row.setter
    def previous_row(self, previous_row:int) -> None:
        self.__previous_row = previous_row
    
    @property
    def next_row(self) -> int:
        return (self.__row + self.speed) if self.direction == "down" else (self.__row - self.speed) if self.direction == "up" else self.__row

    @property
    def is_solid(self) -> bool:
        return self.__is_solid
    
    @is_solid.setter
    def is_solid(self, is_solid:bool) -> None:
        self.__is_solid:bool = is_solid