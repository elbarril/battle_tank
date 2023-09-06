from MovableMapObject import MovableMapObject
from Direction import Direction
from Constants import MAP_OBJECT_MIN_SIZE, BULLET_IMAGE_FILENAME

class Bullet(MovableMapObject):
    def __init__(self, row:int, column:int, direction:Direction):
        super().__init__(row, column, MAP_OBJECT_MIN_SIZE, BULLET_IMAGE_FILENAME, direction)
        self.can_destroy = True