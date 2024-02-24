from models.generic.Size import Size
from constants.map import MAP_WIDTH, MAP_HEIGHT

class MapSize(Size):
    def __init__(self, width=MAP_WIDTH, height=MAP_HEIGHT):
        super().__init__(width, height)
