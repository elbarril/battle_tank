class Level:
    from model.game.Bot import Bot
    from model.game.entity.Static import Static
    
    def __init__(self, id:int, statics:list[Static], bots:list[Bot]) -> None:
        self.__id = id
        self.__statics = statics
        self.__bots = bots

    @property
    def id(self) -> int:
        return self.__id

    @property
    def statics(self) -> list[Static]:
        return self.__statics

    @property
    def bots(self) -> list[Bot]:
        return self.__bots