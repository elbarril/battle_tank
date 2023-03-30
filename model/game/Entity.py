from model.game.board.Position import Position

class Entity():
    def __init__(self, position:Position, is_solid:bool):
        self.__position:Position = position
        self.__is_solid:bool = is_solid

    @property
    def position(self) -> Position:
        return self.__position

    @position.setter
    def position(self, position:Position) -> None:
        self.__position = position

    @property
    def is_solid(self) -> bool:
        return self.__is_solid
    
    @is_solid.setter
    def is_solid(self, is_solid:bool) -> None:
        self.__is_solid:bool = is_solid

    def __repr__(self):
        return f"(position={repr(self.position)}, is_solid={str(self.is_solid)})"