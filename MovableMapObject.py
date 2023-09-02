from MapObject import MapObject
from Position import Position
from Direction import Direction

class MovableMapObject(MapObject):
    def __init__(self, row:int, column:int, width:int, height:int, image_url:str):
        super().__init__(row, column, width, height, image_url)
        self.__direction = Direction()
    
    def move(self):
        self.position = self.next_position
        return self

    @property
    def next_position_area(self) -> tuple[int]:
        left = self.next_position.x - self.size.width
        top = self.next_position.y - self.size.height
        right = self.next_position.x + self.size.width
        bottom = self.next_position.y + self.size.height
        
        return(left, top, right, bottom)
    
    @property
    def next_position(self):
        row, column = self.position.row, self.position.column
        return Position(row+self.direction.row, column+self.direction.column)
    
    @property
    def direction(self) -> Direction:
        return self.__direction
    
    @direction.setter
    def direction(self, direction:Direction) -> None:
        self.__direction = direction