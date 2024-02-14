from model.MapObject import MapObject
from view.Image import Image
from abc import ABC, abstractmethod

class MapObjectView(ABC):
    def __init__(self, model:MapObject, image:Image):
        self.__model = model
        self.__image = image

    @property
    @abstractmethod
    def model(self): return self.__model

    @property
    def image(self): return self.__image

    @image.setter
    def image(self, image:Image): self.__image = image

    @property
    def x0(self): return self.__model.position.x

    @property
    def x1(self): return self.__model.position.x + self.__model.side

    @property
    def y0(self): return self.__model.position.y

    @property
    def y1(self): return self.__model.position.y + self.__model.side