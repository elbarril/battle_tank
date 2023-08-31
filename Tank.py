from MovableMapObject import MovableMapObject
from Bullet import Bullet

class Tank(MovableMapObject):
    def __init__(self, row:int, column:int, width:int, height:int, image_url:str):
        super().__init__(row, column, width, height, image_url)

    def shoot(self) -> Bullet:
        row = self.position.row + self.direction.row * self.size.height
        column = self.position.column + self.direction.column * self.size.width
        return Bullet(row, column, self.direction, self)