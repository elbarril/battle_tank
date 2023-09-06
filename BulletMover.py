from Map import Map
from Bullet import Bullet
from threading import Thread
import time

class BulletMover:
    def __init__(self, map:Map):
        self.__bullets:list[Bullet] = []
        self.__map = map
        self.__thread:Thread = None
        
    @property
    def bullets(self) -> list[Bullet]:
        return self.__bullets
    
    def add(self, bullet:Bullet):
        self.__map.add(bullet)
        self.__bullets.append(bullet)
        return self

    def run(self) -> None:
        if len(self.__bullets) and not self.__thread_is_running():
            self.__run_thread()
    
    def __remove(self, bullet:Bullet):
        self.__map.remove(bullet)
        self.__bullets.remove(bullet)
    
    def __move_bullets(self) -> None:
        while len(self.__bullets):
            for bullet in self.__bullets:
                collided_objects = self.__map.get_objects_in_area(bullet.next_position_area)
                if bullet in collided_objects: collided_objects.remove(bullet)
                if collided_objects:
                    self.__remove(bullet)
                    self.__map.remove(collided_objects[0])
                elif self.__map.is_out_of_limits(bullet.next_position_area): self.__remove(bullet)
                else: self.__map.move(bullet)
            time.sleep(.05)

    def __thread_is_running(self) -> bool:
        if self.__thread and self.__thread.is_alive():return True
        
    def __run_thread(self):
        self.__thread = Thread(target=self.__move_bullets)
        self.__thread.daemon = True
        self.__thread.start()