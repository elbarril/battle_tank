from Map import Map
from MovableMapObject import MovableMapObject
from threading import Thread
import time
from Direction import *

class BotMover:
    def __init__(self, map:Map):
        self.__bot_tanks:list[MovableMapObject] = []
        self.__map = map
        self.__thread:Thread = None
        
    @property
    def bot_tanks(self) -> list[MovableMapObject]:
        return self.__bot_tanks
    
    def add(self, object:MovableMapObject):
        self.__bot_tanks.append(self.__map.add(object))
        return self

    def run(self) -> None:
        if len(self.__bot_tanks) and not self.__thread_is_running():
            self.__run_thread()
    
    def __remove(self, object:MovableMapObject):
        self.__bot_tanks.pop(self.__bot_tanks.index(self.__map.remove(object)))
    
    def __move_bot_tanks(self) -> None:
        while len(self.__bot_tanks):
            for bot_tank in self.__bot_tanks:
                next_area = bot_tank.next_position_area
                if not self.__map.is_out_of_limits(next_area):
                    collided_objects = self.__map.get_objects_in_area(next_area)
                    if bot_tank in collided_objects: collided_objects.remove(bot_tank)
                    if not len(collided_objects):
                        self.__map.move(bot_tank)
            time.sleep(.1)

    def __thread_is_running(self) -> bool:
        if self.__thread and self.__thread.is_alive():return True
        
    def __run_thread(self):
        self.__thread = Thread(target=self.__move_bot_tanks)
        self.__thread.daemon = True
        self.__thread.start()