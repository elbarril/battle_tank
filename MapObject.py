from Position import Position
from tkinter import PhotoImage
from Dimension import Dimension

class MapObject:
    def __init__(self, row:int, column:int, width:int, height:int, image_file:str):
        self.__position = Position(row, column)
        self.__size = Dimension(width, height)
        self.__image = PhotoImage(file=image_file)

    @property
    def image(self) -> str:
        return self.__image

    @property
    def size(self) -> Dimension:
        return self.__size

    @size.setter
    def size(self, size:Dimension) -> None:
        self.__size = size
    
    @property
    def position(self) -> Position:
        return self.__position
    
    @position.setter
    def position(self, position:Position) -> None:
        self.__position = position
