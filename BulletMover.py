from Map import Map
from MovableMapObject import MovableMapObject
from threading import Thread
import time

class BulletMover:
    def __init__(self, map:Map):
        self.__bullets:list[MovableMapObject] = []
        self.__map = map
        self.__thread:Thread = None
        
    @property
    def bullets(self) -> list[MovableMapObject]:
        return self.__bullets
    
    def add(self, object:MovableMapObject):
        self.__bullets.append(self.__map.add(object))
        return self

    def run(self) -> None:
        if len(self.__bullets) and not self.__thread_is_running():
            self.__run_thread()
    
    def __remove(self, object:MovableMapObject):
        self.__bullets.pop(self.__bullets.index(self.__map.remove(object)))
    
    def __move_bullets(self) -> None:
        while len(self.__bullets):
            for bullet in self.__bullets:
                self.__map.move(bullet)
                collided_objects = self.__map.get_objects_in_area(bullet.area)
                if bullet in collided_objects: collided_objects.remove(bullet)
                if collided_objects:
                    if collided_objects[0].can_be_destroyed: self.__map.remove(collided_objects[0])
                    self.__remove(bullet)
                elif self.__map.is_out_of_limits(bullet.area): self.__remove(bullet)
            time.sleep(.05)

    def __thread_is_running(self) -> bool:
        if self.__thread and self.__thread.is_alive():return True
        
    def __run_thread(self):
        self.__thread = Thread(target=self.__move_bullets)
        self.__thread.daemon = True
        self.__thread.start()