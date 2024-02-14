from model.SingleMapObject import SingleMapObject, Position

class MovableSingleMapObject(SingleMapObject):
    def __init__(self, position:Position, side:int, direction:str):
        super().__init__(position, side)
        self.__direction = direction

    @property
    def direction(self): return self.__direction
    
    @direction.setter
    def direction(self, direction:str):
        self.__direction = direction