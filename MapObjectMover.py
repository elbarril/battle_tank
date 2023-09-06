from Map import Map
from Bullet import Bullet
from Tank import Tank
from MoverThread import MoverThread
from Direction import Direction, DIRECTIONS
from Constants import (
    UP_DIRECTION_KEY,
    DOWN_DIRECTION_KEY,
    LEFT_DIRECTION_KEY,
    RIGHT_DIRECTION_KEY
)

import time
import random

class MapObjectMover:
    def __init__(self, map:Map):
        self.__bullets:list[Bullet] = []
        self.__tanks:list[Tank] = []
        self.__map = map
        self.directions = [Direction(d) for d in DIRECTIONS.keys()]
        self.__bullet_mover = MoverThread(self.__move_bullets)
        self.__tank_mover = MoverThread(self.__move_tanks)
    
    def add_player_tank(self, player_tank:Tank):
        self.__player_tank = player_tank
    
    def add_bullet(self, bullet:Bullet):
        self.__map.add(bullet)
        self.__bullets.append(bullet)
        if not self.__bullet_mover.is_running():
            self.__bullet_mover.run()
    
    def add_tank(self, tank:Tank):
        self.__map.add(tank)
        self.__tanks.append(tank)
        if not self.__tank_mover.is_running():
            self.__tank_mover.run()
    
    def __move_bullets(self) -> None:
        while len(self.__bullets):
            for bullet in self.__bullets:
                collided_objects = self.__map.get_objects_in_area(bullet.next_position_area)
                if bullet in collided_objects: collided_objects.remove(bullet)
                if bullet.creator in collided_objects: collided_objects.remove(bullet.creator)
                if collided_objects:
                    self.__map.remove(bullet)
                    self.__bullets.remove(bullet)
                    collided = collided_objects[0]
                    if collided.can_be_destroyed: self.__map.remove(collided)
                    if isinstance(collided, Tank): self.__tanks.remove(collided)
                elif self.__map.is_out_of_limits(bullet.next_position_area):
                    self.__map.remove(bullet)
                    self.__bullets.remove(bullet)
                else: self.__map.move(bullet)
            time.sleep(.05)
            self.__map.update()
            
    def __move_tanks(self) -> None:
        wait = .05
        seconds = 0
        while len(self.__tanks):
            for tank in self.__tanks:
                next_direction = tank.direction
                decision = 1
                if self.__player_tank.row == tank.row or self.__player_tank.column == tank.column:
                    decision = random.choice([1,0])
                
                if self.__player_tank.row == tank.row:
                    next_direction = Direction(RIGHT_DIRECTION_KEY) if self.__player_tank.column > tank.column else Direction(LEFT_DIRECTION_KEY)
                elif self.__player_tank.column == tank.column:
                    next_direction = Direction(DOWN_DIRECTION_KEY) if self.__player_tank.row > tank.row else Direction(UP_DIRECTION_KEY)
                elif seconds > wait*10:
                    seconds = 0
                    another_directions = self.directions[:]
                    another_directions.remove(tank.direction)
                    next_direction = random.choice(another_directions)
                
                if not decision:
                    bullet = tank.shoot()
                    self.add_bullet(bullet)
                
                next_area = tank.next_position_area
                
                if tank.direction != next_direction:
                    self.__map.remove(tank)
                    tank.rotate(next_direction)
                    self.__map.add(tank)
                elif not self.__map.is_out_of_limits(next_area):
                    collided_objects = self.__map.get_objects_in_area(next_area)
                    if tank in collided_objects: collided_objects.remove(tank)
                    if not len(collided_objects):
                        self.__map.move(tank)

            time.sleep(wait)
            seconds += wait
            self.__map.update()