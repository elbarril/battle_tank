from models.generic.Size import Size

MAP_WIDTH = 10
MAP_HEIGHT = 10

class MapSize(Size):
    def __init__(self, width=MAP_WIDTH, height=MAP_HEIGHT):
        super().__init__(width, height)
