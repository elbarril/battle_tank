from model.Player import Player, Tank
from threading import Thread
import time
import random
from constants import BOT_MAP_CODE, DIRECTION_KEYS

class Bot(Player):
    def __init__(self, ia):
        super().__init__()
        self.__tanks:list[Tank] = []
        self.__ia = ia

    def add_tank(self, tank:Tank):
        tank.code = BOT_MAP_CODE
        self.__tanks.append(tank)

    def remove_tank(self, tank:Tank):
        self.__tanks.remove(tank)

    def play(self):
        self.__bot = Thread(target=self.__ia)
        self.__bot.daemon = True
        self.__bot.start()

    def __bot_ia(self):
        while len(self.__tanks):
            for tank in self.__tanks:
                time.sleep(.5)
                move = lambda t=tank,dk=random.choice(DIRECTION_KEYS): self.__game.move_tank(t,dk)
                shoots = lambda t=tank: self.__game.tank_shoots(t)
                action = random.choice([move, shoots])
                action()