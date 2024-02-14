from view.SingleMapObjectView import SingleMapObjectView, Image
from model.MultipleMapObject import MultipleMapObject

class MultipleMapObjectView(SingleMapObjectView):
    def __init__(self, model:MultipleMapObject, image:Image):
        super().__init__(model, image)
        self.__model = model

    @property
    def model(self): return self.__model