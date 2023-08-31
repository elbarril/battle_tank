from Map import Map
from MovableMapObject import MovableMapObject
from threading import Thread
import time

class Mover:
    def __init__(self, map:Map):
        self.__objects:list[MovableMapObject] = []
        self.__map = map
        self.__thread:Thread = None
        
    @property
    def objects(self) -> list[MovableMapObject]:
        return self.__objects
        
    @property
    def map(self) -> Map:
        return self.__map
    
    def add(self, object:MovableMapObject) -> None:
        self.__objects.append(object)
        self.__map.add(object)
        if not self.__thread_is_running():
            self.__run_thread()
    
    def __move_objects(self) -> None:
        while (len(self.__objects)):
            for obj in self.__objects:
                collided_object = self.__map.get_collided_object(obj)
                if self.__map.can_move(obj) and not collided_object:
                    self.__map.move(obj)
                else:
                    self.__map.remove(obj)
                    self.__objects.pop(self.__objects.index(obj))
                    if collided_object:
                        self.__map.remove(collided_object)
            time.sleep(.05)

    def __thread_is_running(self) -> bool:
        if self.__thread and self.__thread.is_alive():return True
        
    def __run_thread(self):
        self.__thread = Thread(target=self.__move_objects)
        self.__thread.daemon = True
        self.__thread.start()