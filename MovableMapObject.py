from MapObject import MapObject
from Position import Position
from Direction import Direction

class MovableMapObject(MapObject):
    def __init__(self, row:int, column:int, width:int, height:int, image_url:str):
        super().__init__(row, column, width, height, image_url)
        self.__direction = Direction()
    
    def move(self) -> None:
        row, column = self.position.row, self.position.column
        self.position = Position(row+self.direction.row, column+self.direction.column)
        
    @property
    def direction(self) -> Direction:
        return self.__direction
    
    @direction.setter
    def direction(self, direction:Direction) -> None:
        self.__direction = direction