from model.game.level.Level import Level
from model.game.board.Position import Position
    
class LevelFactory:
    __instance = None
    
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.initialize()
        return cls.__instance

    @classmethod
    def initialize(cls):
        from model.game.Bot import Bot
        from model.game.entity.movable.Tank import Tank
        from model.game.entity.Static import Static
        from model.game.entity.static.classes.STATIC_CLASSES import STATIC_CLASSES
        from model.Constants import LEVELS, FIRST_LEVEL

        cls.__next_level:int = FIRST_LEVEL

        cls.__level_statics:list[Static] = []
        cls.__levels:dict[int, Level] = {}

        for ID, LEVEL_DATA in enumerate(LEVELS):
            for row, columns in enumerate(LEVEL_DATA["statics"]):
                for column, static_id in enumerate(columns):
                    static = STATIC_CLASSES[static_id].value(Position(row, column))
                    cls.__level_statics.append(static)

            level = Level(
                id = ID,
                statics = cls.__level_statics,
                bots = [Bot(Tank(Position(bot["row"], bot["column"]), bot["direction"], bot["speed"])) for bot in LEVEL_DATA["bots"]]
            )

            cls.__levels.setdefault(ID, level)
                    
        cls.__instance = cls()

    @property
    def next_level(self) -> Level:
        from model.Constants import EXCEPTIONS_MESSAGES, EXCODE_LWNC

        if self.__levels.get(self.__next_level) is None:
            raise Exception(EXCEPTIONS_MESSAGES[EXCODE_LWNC].format(level=self.__next_level))
        return self.__levels.get(self.__next_level)

    @property
    def has_next_level(self) -> bool:
        return self.__next_level in self.__levels
