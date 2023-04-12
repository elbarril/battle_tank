
from model.game.CollisionManager import CollisionManager
class Level:
    from model.game.Board import Board
    
    def __init__(self, id:int, board:Board) -> None:
        self.__id = id
        self.__board = board

    @property
    def id(self) -> int:
        return self.__id

    @property
    def board(self) -> Board:
        return self.__board
    
    def play_bullets(self) -> None:
        if self.board.has_bullets:
            for bullet in self.board.bullets:
                if self.board.is_valid_position(bullet.next_position):
                    collided_entity = CollisionManager.hits(self.board.get_square(bullet.next_position))
                    if not collided_entity:
                        self.board.remove_entity(bullet)
                        bullet.move()
                        self.board.add_entity(bullet)
                    else:
                        self.board.remove_entity(bullet)
                else:
                    self.board.remove_entity(bullet)