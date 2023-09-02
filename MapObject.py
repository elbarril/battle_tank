from Position import Position
from tkinter import PhotoImage
from Dimension import Dimension

class MapObject:
    def __init__(self, row:int, column:int, width:int, height:int, image_file:str):
        self.__position = Position(row, column)
        self.__size = Dimension(width, height)
        self.__image = PhotoImage(file=image_file)
        self.__can_destroy = self.__can_be_destroyed = False

    @property
    def can_destroy(self) -> bool:
        return self.__can_destroy

    @can_destroy.setter
    def can_destroy(self, can_destroy:bool) -> None:
        self.__can_destroy = can_destroy

    @property
    def can_be_destroyed(self) -> bool:
        return self.__can_be_destroyed

    @can_be_destroyed.setter
    def can_be_destroyed(self, can_be_destroyed:bool) -> None:
        self.__can_be_destroyed = can_be_destroyed
    
    @property
    def image(self) -> str:
        return self.__image

    @property
    def area(self) -> tuple[int]:
        left = self.position.x - self.size.width / 2
        top = self.position.y - self.size.height / 2
        right = self.position.x + self.size.width / 2
        bottom = self.position.y + self.size.height / 2
        
        return(left, top, right, bottom)
    
    @property
    def size(self):
        return self.__size
    
    @property
    def position(self) -> Position:
        return self.__position
    
    @position.setter
    def position(self, position:Position) -> None:
        self.__position = position
