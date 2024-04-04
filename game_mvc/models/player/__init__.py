from models.map import MovableObjectDirections

from constants import TO_STRING_PLAYER
from constants import FIRST_PLAYER, SECOND_PLAYER
from views import TK_KEYBOARD

class AbstractPlayer:
    def __init__(self):
        self.__tank = None
    
    @property
    def tank(self):
        return self.__tank

    def set_tank(self, tank):
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

class HumanPlayer(AbstractPlayer):
    def __init__(self, number):
        self.__number = number
        self.__action_keys = {
            "movement": [],
            "shoot": []
        }

    @property
    def number(self):
        return self.__number
    
    @property
    def movement_keys(self):
        return self.__action_keys["movement"]
    
    @property
    def shoot_keys(self):
        return self.__action_keys["shoot"]

    def set_movement_key(self, key, direction):
        movements_keys = self.__action_keys["movement"]
        self.__action_keys.update({"movement": movements_keys + [(key, direction)]})

    def set_shoot_key(self, key):
        shoot_keys = self.__action_keys["shoot"]
        self.__action_keys.update({"shoot": shoot_keys + [key]})

    def __str__(self):
        return TO_STRING_PLAYER % self.number

class PlayerOne(HumanPlayer):
    def __init__(self):
        super().__init__(FIRST_PLAYER)
        self.set_movement_key(TK_KEYBOARD.UP, MovableObjectDirections.UP)
        self.set_movement_key(TK_KEYBOARD.DOWN, MovableObjectDirections.DOWN)
        self.set_movement_key(TK_KEYBOARD.LEFT, MovableObjectDirections.LEFT)
        self.set_movement_key(TK_KEYBOARD.RIGHT, MovableObjectDirections.RIGHT)
        self.set_shoot_key(TK_KEYBOARD.M)

class PlayerTwo(HumanPlayer):
    def __init__(self):
        super().__init__(SECOND_PLAYER)
        self.set_movement_key(TK_KEYBOARD.W, MovableObjectDirections.UP)
        self.set_movement_key(TK_KEYBOARD.S, MovableObjectDirections.DOWN)
        self.set_movement_key(TK_KEYBOARD.A, MovableObjectDirections.LEFT)
        self.set_movement_key(TK_KEYBOARD.D, MovableObjectDirections.RIGHT)
        self.set_shoot_key(TK_KEYBOARD.SPACE)