from model.game.entity.Movable import Movable
from model.game.board.Square import Square
from model.game.entity.Static import Static
from model.game.board.Position import Position

class Board:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.initialize()
        return cls.__instance

    @classmethod
    def initialize(cls):
        from model.Constants import SQUARES_COLUMNS, SQUARES_ROWS
        cls.__squares:list[list[Square]] = [[Square() for _ in range(SQUARES_COLUMNS)] for _ in range(SQUARES_ROWS)]
        
        cls.__instance = cls()

    def is_valid_position(self, position:Position) -> bool:
        return (position.row >= 0 and position.column >= 0) and (position.row < len(self.squares) and position.column < len(self.squares[position.row]))

    @property
    def squares(self) -> list[list[Square]]:
        return self.__squares
    
    def get_square(self, position:Position) -> Square:
        return self.squares[position.row][position.column]
    
    def add_entity(self, entity:Movable|Static) -> None:
        self.squares[entity.position.row][entity.position.column].add(entity)
    
    def remove_entity(self, entity:Movable|Static) -> None:
        if isinstance(entity, Movable):
            self.squares[entity.position.row][entity.position.column].remove(entity)