from model.game.board.Square import Square

class CollisionManager:

    @classmethod
    def hits(cls, square:Square):
        return square.tank or square.bullet or square.element.is_solid