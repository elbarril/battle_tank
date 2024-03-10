from utils.Size import Size

class MapSize(Size):
    def __str__(self):
        return f"MapSize(width={self.width}, height={self.height})"