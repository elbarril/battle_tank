from threading import Thread
from MovableMapObject import MovableMapObject
import time

class MoverThread:
    def __init__(self, move_callback):
        self.__movable_objects:list[MovableMapObject] = []
        self.__move_callback = move_callback
        self.__thread = Thread(target=self.__moving_loop)
    
    def __moving_loop(self):
        while len(self.__movable_objects):
            for obj in self.__movable_objects:
                self.__move_callback(obj)
            time.sleep(.05)

    def add(self, movable:MovableMapObject):
        self.__movable_objects.append(movable)

    def remove(self, movable:MovableMapObject):
        self.__movable_objects.remove(movable)

    def has(self, movable:MovableMapObject):
        return movable in self.__movable_objects
    
    def is_running(self) -> bool:
        if self.__thread and self.__thread.is_alive():return True
            
    def run(self):
        self.__thread = Thread(target=self.__moving_loop)
        self.__thread.daemon = True
        self.__thread.start()

    def stop(self):        
        self.__thread.join()