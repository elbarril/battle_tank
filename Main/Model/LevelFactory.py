from Main.Model.Level import Level
from Main.Model.Bot import Bot
from Main.Model.ElementFactory import ElementFactory
from Main.Model.MapElement import MapElement
from Main.Model.Constants import LEVELS, FIRST_LEVEL, EXCEPTIONS_MESSAGES, EXCODE_LWNC, EXCODE_FLWNC, EXCODE_VINN
from typing import Union
    
class LevelFactory:
    __instance = None
    __element_factory:ElementFactory = None
    __levels:dict[Union[str, int], Level] = {}
    __next_level:Union[str, int] = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.initialize()
        return cls.__instance

    @classmethod
    def initialize(cls):
        cls.__instance = cls()
        cls.__element_factory = ElementFactory.get_instance()
        for ID, LEVEL_DATA in LEVELS.items():
            cls.__register_level(ID, LEVEL_DATA)
    
    @classmethod
    def __register_level(cls, level_id:str, level_data:dict[str, str]) -> None:
        level = Level(
            id = level_id,
            elements = cls.__get_level_elements(level_data["elements"]),
            bots = cls.__get_level_bots(level_data["bots"])
        )
        cls.__levels.setdefault(level_id, level)

    @classmethod
    def __get_level_elements(cls, elements:list[list[str]]) -> list[MapElement]:
        level_elements:list[MapElement] = []
        for row, columns in enumerate(elements):
            for column, element_id in enumerate(columns):
                level_elements.append(cls.__element_factory.get_element(element_id, row, column))
        return level_elements

    @classmethod
    def __get_level_bots(cls, bots) -> list[Bot]:
        level_bots:list[Bot] = [Bot(bot) for bot in bots]
        return level_bots

    @property
    def first_level(self) -> Level:
        self.__next_level = FIRST_LEVEL
        if self.__levels.get(self.__next_level) is None:
            raise Exception(EXCEPTIONS_MESSAGES[EXCODE_LWNC].format(level=self.__next_level))
        return self.__levels.get(self.__next_level)
        
    
    @property
    def next_level(self) -> Level:
        if self.__next_level is None:
            raise Exception(EXCEPTIONS_MESSAGES[EXCODE_FLWNC])
        self.__update_next_level()
        if self.__levels.get(self.__next_level) is None:
            raise Exception(EXCEPTIONS_MESSAGES[EXCODE_LWNC].format(level=self.__next_level))
        return self.__levels.get(self.__next_level)

    @property
    def has_next_level(self) -> bool:
        if self.__next_level in self.__levels:
            return True
        return False
    
    def __update_next_level(self):
        try:
            self.__next_level = (int(self.__next_level) + 1)
        except ValueError:
            print(EXCEPTIONS_MESSAGES[EXCODE_VINN].format(variable=self.__next_level))
        self.__next_level = str(self.__next_level)
