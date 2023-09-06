from Map import Map
from Player import Player
from Bullet import Bullet
from Tank import Tank
from threading import Thread
import time
from Direction import Direction, DIRECTIONS
from Constants import (
    UP_DIRECTION_KEY,
    DOWN_DIRECTION_KEY,
    LEFT_DIRECTION_KEY,
    RIGHT_DIRECTION_KEY
)
from random import choice
class BotMover:
    def __init__(self, map:Map):
        self.__bot_tanks:list[Tank] = []
        self.__map = map
        self.__thread:Thread = None
        
    @property
    def bot_tanks(self) -> list[Tank]: return self.__bot_tanks
    
    def set_player(self, player:Player): self.__player = player
    
    def add(self, tank:Tank):
        self.__map.add(tank)
        self.__bot_tanks.append(tank)
        return self

    def run(self) -> None:
        if len(self.__bot_tanks) and not self.__thread_is_running():
            self.__run_thread()
    
    def __remove(self, tank:Tank):
        self.__map.remove(tank)
        self.__bot_tanks.remove(tank)
    
    def __move_bot_tanks(self) -> None:
        wait = seconds = 0.05
        while len(self.__bot_tanks):
            for bot_tank in self.__bot_tanks:
                next_direction = bot_tank.direction

                if self.__player.tank.row == bot_tank.row:
                    next_direction = Direction(RIGHT_DIRECTION_KEY) if self.__player.tank.column > bot_tank.column else Direction(LEFT_DIRECTION_KEY)
                elif self.__player.tank.column == bot_tank.column:
                    next_direction = Direction(DOWN_DIRECTION_KEY) if self.__player.tank.row > bot_tank.row else Direction(UP_DIRECTION_KEY)
                elif seconds > 1 :
                    seconds = 0
                    next_direction = Direction(choice(list(DIRECTIONS.keys())))
                
                next_area = bot_tank.next_position_area
                
                if bot_tank.direction != next_direction:
                    self.__map.remove(bot_tank)
                    bot_tank.rotate(next_direction)
                    self.__map.add(bot_tank)
                elif not self.__map.is_out_of_limits(next_area):
                    collided_objects = self.__map.get_objects_in_area(next_area)
                    if bot_tank in collided_objects: collided_objects.remove(bot_tank)
                    if not len(collided_objects):
                        self.__map.move(bot_tank)
                    elif Bullet in [type(obj) for obj in collided_objects]:
                        self.__remove(bot_tank)

            time.sleep(wait)
            seconds += wait

    def __thread_is_running(self) -> bool:
        if self.__thread and self.__thread.is_alive():return True
        
    def __run_thread(self):
        self.__thread = Thread(target=self.__move_bot_tanks)
        self.__thread.daemon = True
        self.__thread.start()