from Image import Image

class MapObject:
    def __init__(self, row:int, column:int, size:int, image_filename:str):
        self.__row = row
        self.__column = column
        self._radio = size / 2
        self.__image = Image(image_filename)
        self.__can_destroy = self.__can_be_destroyed = False

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image:Image):
        self.__image = image

    @property
    def can_move(self):
        return self.__can_move

    @can_move.setter
    def can_move(self, can_move):
        self.__can_move = can_move
    
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
    def row(self) -> int:
        return self.__row
    
    @row.setter
    def row(self, row:int) -> None:
        self.__row = row
    
    @property
    def column(self) -> int:
        return self.__column
    
    @column.setter
    def column(self, column:int) -> None:
        self.__column = column

    @property
    def left(self) -> int:
        return self.column - self._radio

    @property
    def top(self) -> int:
        return self.row - self._radio

    @property
    def right(self) -> int:
        return self.column + self._radio

    @property
    def bottom(self) -> int:
        return self.row + self._radio