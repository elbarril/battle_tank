from Main.Model.Brick import Brick
from Main.Model.Path import Path
from Main.Model.Stone import Stone
from Main.Model.Water import Water
from Main.Model.Metal import Metal
from Main.Model.Earth import Earth
from Main.Model.Bush import Bush
from Main.Model.MapElement import MapElement

class ElementFactory:
    __instance = None
    __elements:dict[str, MapElement] = {}

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.initialize()
        return cls.__instance

    @classmethod
    def initialize(cls):
        cls.__instance = cls()
        cls.__register_element("B", Brick)
        cls.__register_element("P", Path)
        cls.__register_element("S", Stone)
        cls.__register_element("W", Water)
        cls.__register_element("M", Metal)
        cls.__register_element("E", Earth)
        cls.__register_element("F", Bush)

    @classmethod
    def __register_element(cls, element_id:str, element_class) -> None:
        cls.__elements[element_id] = element_class

    def get_element(self, element_id:str, row:int, column:int) -> MapElement:
        return self.__elements[element_id](row, column)