from model.SingleMapObject import SingleMapObject
from view.MapObjectView import MapObjectView, Image

class SingleMapObjectView(MapObjectView):
    def __init__(self, model:SingleMapObject, image:Image):
        super().__init__(model, image)

    @property
    def model(self): return super().model