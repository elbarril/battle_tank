from view.MultipleMapObjectView import MultipleMapObjectView, MultipleMapObject, Image
from constants import WALL_MAP_CODE

class WallView(MultipleMapObjectView):
    def __init__(self, model:MultipleMapObject, image:Image):
        super().__init__(model, image)
        self.code = WALL_MAP_CODE