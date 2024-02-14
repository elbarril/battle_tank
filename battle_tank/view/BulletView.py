from view.MovableSingleMapObjectView import MovableSingleMapObjectView, MovableSingleMapObject, Image
from constants import BULLET_MAP_CODE

class BulletView(MovableSingleMapObjectView):
    def __init__(self, model:MovableSingleMapObject, image:Image):
        super().__init__(model, image)
        self.code = BULLET_MAP_CODE