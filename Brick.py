from MapObject import MapObject
from Constants import MAP_OBJECT_MIN_SIZE, BRICK_IMAGE_FILENAME

class Brick(MapObject):
    def __init__(self, row:int, column:int):
        super().__init__(row, column, MAP_OBJECT_MIN_SIZE, BRICK_IMAGE_FILENAME)
        
        self.can_be_destroyed = True