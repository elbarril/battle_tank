from models.map.MapObjectDirection import *
from views import TK_KEYBOARD
from models.map.objects.Tank import Tank
from models.map import Map

class AbstractPlayer:
    def __init__(self, tank:Tank=None) -> None:
        self.__tank = tank
    
    @property
    def tank(self) -> Tank:
        return self.__tank

    def set_tank(self, tank:Tank) -> None:
        self.__tank = tank

    def move_tank(self, map:Map, direction:MapObjectDirection) -> None:
        if self.__tank.position + direction in map:
            del map[self.__tank.position*self.__tank.size]
            self.__tank.position = self.__tank.position + direction
            map[self.__tank.position*self.__tank.size] = self.__tank

class BotPlayer(AbstractPlayer):
    pass

class BotPlayerCollection:
    def __init__(self):
        self.__bots = []

    def set_bot(self, tank):
        bot = BotPlayer()
        bot.set_tank(tank)
        self.__bots.append(bot)

from enum import Enum
class PlayerAction(Enum):
    MOVEMENT = 1
    SHOOT = 2

class PlayerActionKey:
    def __init__(self, key:str, value=None):
        self.__key = key
        self.__value = value

    @property
    def key(self) -> str: return self.__key

    @property
    def value(self) -> str: return self.__value

class HumanPlayer(AbstractPlayer):
    def __init__(self, number:int) -> None:
        self.__number = number
        self.__actions = {
            PlayerAction.MOVEMENT: [],
            PlayerAction.SHOOT: []
        }

    @property
    def number(self) -> int:
        return self.__number
    
    @property
    def movement(self) -> list[PlayerActionKey]:
        return self.__actions[PlayerAction.MOVEMENT]
    
    @property
    def shoot(self) -> list[PlayerActionKey]:
        return self.__actions[PlayerAction.SHOOT]

    def set_movement_key(self, key:str, direction:MapObjectDirection) -> None:
        action = PlayerActionKey(key, direction)
        self.__actions[PlayerAction.MOVEMENT].append(action)

    def set_shoot_key(self, key:str) -> None:
        action = PlayerActionKey(key)
        self.__actions[PlayerAction.SHOOT].append(action)

class PlayerOne(HumanPlayer):
    def __init__(self) -> None:
        super().__init__(1)
        self.set_movement_key(TK_KEYBOARD.UP, UP)
        self.set_movement_key(TK_KEYBOARD.DOWN, DOWN)
        self.set_movement_key(TK_KEYBOARD.LEFT, LEFT)
        self.set_movement_key(TK_KEYBOARD.RIGHT, RIGHT)
        self.set_shoot_key(TK_KEYBOARD.M)

class PlayerTwo(HumanPlayer):
    def __init__(self) -> None:
        super().__init__(2)
        self.set_movement_key(TK_KEYBOARD.W, UP)
        self.set_movement_key(TK_KEYBOARD.S, DOWN)
        self.set_movement_key(TK_KEYBOARD.A, LEFT)
        self.set_movement_key(TK_KEYBOARD.D, RIGHT)
        self.set_shoot_key(TK_KEYBOARD.SPACE)