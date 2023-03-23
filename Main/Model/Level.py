from Main.Model.Bot import Bot
from Main.Model.Static import Static

class Level:
    def __init__(self, id:str, elements:list[Static], bots:list[Bot]) -> None:
        self.__id = id
        self.__elements = elements
        self.__bots = bots

    @property
    def id(self) -> str:
        return self.__id

    @property
    def elements(self) -> list[Static]:
        return self.__elements

    @property
    def bots(self) -> list[Bot]:
        return self.__bots