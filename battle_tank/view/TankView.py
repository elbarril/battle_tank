from model.Tank import Tank
from view.MovableSingleMapObjectView import MovableSingleMapObjectView, Image
from view.BulletView import BulletView

class TankView(MovableSingleMapObjectView):
    def __init__(self, model:Tank, images:list[Image], bullet_images:list[Image]):
        super().__init__(model, images)
        self.__model = model
        self.__bullet_images = bullet_images

    @property
    def model(self): return self.__model

    def shoot(self): return BulletView(self.model.shoot(), self.__bullet_images)