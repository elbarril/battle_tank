from model.game.entity.Movable import Movable
from model.game.board.Square import Square
from model.game.entity.Static import Static
from model.game.entity.movable.Bullet import Bullet
from model.game.Bot import Bot
from model.game.board.Position import Position

class Board:
    __bots:list[Bot] = []
    __bullets:list[Bullet] = []

    def __init__(self):
        from model.Constants import SQUARES_COLUMNS, SQUARES_ROWS
        self.__squares:list[list[Square]] = [[Square() for _ in range(SQUARES_COLUMNS)] for _ in range(SQUARES_ROWS)]

    def is_valid_position(self, position:Position) -> bool:
        return (position.row >= 0 and position.column >= 0) and (position.row < len(self.squares) and position.column < len(self.squares[position.row]))

    @property
    def squares(self) -> list[list[Square]]:
        return self.__squares
    
    @property
    def bots(self) -> list[Bot]:
        return self.__bots
    
    @property
    def bullets(self) -> list[Bullet]:
        return self.__bullets
    
    def get_square(self, position:Position) -> Square:
        return self.squares[position.row][position.column]
    
    def add_entity(self, entity:Movable|Static) -> None:
        self.squares[entity.position.row][entity.position.column].add(entity)
        if isinstance(entity, Bullet):
            self.bullets.append(entity)
        elif isinstance(entity, Bot):
            self.bots.append(entity)
    
    def remove_entity(self, entity:Movable|Static) -> None:
        if isinstance(entity, Movable):
            self.squares[entity.position.row][entity.position.column].remove(entity)
            if isinstance(entity, Bullet):
                self.bullets.remove(entity)
            elif isinstance(entity, Bot):
                self.bots.remove(entity)

    @property
    def has_bots(self) -> bool:
        return True if len(self.bots) else False
    
    @property
    def has_bullets(self) -> bool:
        return True if len(self.bullets) else False