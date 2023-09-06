from MapObject import MapObject
from Direction import Direction
from Image import Image

class MovableMapObject(MapObject):
    def __init__(self, row:int, column:int, size:int, image_filename:str, direction:Direction):
        super().__init__(row, column, size, image_filename + direction.suffix)
        self.__direction = direction
        self.__image_filename = image_filename
    
    def move(self):
        self.row += self.direction.row
        self.column += self.direction.column
        return self
    
    def rotate(self, direction:Direction):
        self.__direction = direction
        self.image = Image(self.__image_filename + direction.suffix)

    @property
    def next_position_area(self) -> tuple[int]:
        left = self.left + self.direction.column
        top = self.top + self.direction.row
        right = self.right + self.direction.column
        bottom = self.bottom + self.direction.row
        
        return(left, top, right, bottom)
    
    @property
    def direction(self) -> Direction:
        return self.__direction

    