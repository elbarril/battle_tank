from views import TK_KEYBOARD

from ..map.object.tank import PlayerTank
from ..map.object import MapObjectDirection as direction


class AbstractPlayer:
    def __init__(self, tank: PlayerTank = None) -> None:
        self.__tank = tank

    @property
    def tank(self) -> PlayerTank:
        return self.__tank

    def set_tank(self, tank: PlayerTank) -> None:
        self.__tank = tank


class BotPlayer(AbstractPlayer):
    pass


class BotPlayerCollection:
    def __init__(self):
        self.__bots = []

    def set_bot(self, tank):
        bot = BotPlayer()
        bot.set_tank(tank)
        self.__bots.append(bot)


class PlayerAction:
    def __init__(self, key: str) -> None:
        self.__key = key

    @property
    def key(self) -> str: return self.__key


class PlayerMovementAction(PlayerAction):
    def __init__(self, key, direction):
        super().__init__(key)
        self.direction = direction


class HumanPlayer(AbstractPlayer):
    def __init__(self, number: int) -> None:
        self.__number = number
        self.__movements: list[PlayerMovementAction] = []
        self.__shooting: list[PlayerAction] = []

    @property
    def number(self) -> int:
        return self.__number

    @property
    def movements(self) -> list[PlayerMovementAction]:
        return self.__movements

    @property
    def shooting(self) -> list[PlayerAction]:
        return self.__shooting

    def set_action(self, key, direction=None):
        if direction:
            self.__movements.append(PlayerMovementAction(key, direction))
        else:
            self.__shooting.append(PlayerAction(key))


class PlayerOne(HumanPlayer):
    def __init__(self) -> None:
        super().__init__(1)
        self.set_action(TK_KEYBOARD.UP, direction.UP)
        self.set_action(TK_KEYBOARD.DOWN, direction.DOWN)
        self.set_action(TK_KEYBOARD.LEFT, direction.LEFT)
        self.set_action(TK_KEYBOARD.RIGHT, direction.RIGHT)
        self.set_action(TK_KEYBOARD.M)


class PlayerTwo(HumanPlayer):
    def __init__(self) -> None:
        super().__init__(2)
        self.set_action(TK_KEYBOARD.W, direction.UP)
        self.set_action(TK_KEYBOARD.S, direction.DOWN)
        self.set_action(TK_KEYBOARD.A, direction.LEFT)
        self.set_action(TK_KEYBOARD.D, direction.RIGHT)
        self.set_action(TK_KEYBOARD.SPACE)
