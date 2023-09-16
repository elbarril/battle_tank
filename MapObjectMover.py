from Player import Player

from Map import Map
from Bullet import Bullet
from Tank import Tank
from MoverThread import MoverThread
from Direction import Direction
from Constants import (
    DIRECTION_UP,
    DIRECTION_DOWN,
    DIRECTION_LEFT,
    DIRECTION_RIGHT
)

import random

class MapObjectMover:
    def __init__(self, map:Map):
        self.__players:list[Player] = []
        self.__map = map

        self.__directions = {d:Direction(d) for d in [DIRECTION_UP,DIRECTION_DOWN,DIRECTION_LEFT,DIRECTION_RIGHT]}

        self.__bullet_mover = MoverThread(self.__move_bullet)
        self.__bot_tank_mover = MoverThread(self.__move_tank)
    
    def add_player(self, player:Player):
        self.__players.append(player)
        self.__map.add(player.tank)
        
    def is_player_alive(self):
        return len([player for player in self.__players if player.is_alive])

    def add_bullet(self, bullet:Bullet):
        self.__bullet_mover.add(bullet)
        self.__map.add(bullet)
        if not self.__bullet_mover.is_running():
            self.__bullet_mover.run()
    
    def add_bot(self, tank:Tank):
        self.__bot_tank_mover.add(tank)
        self.__map.add(tank)
        if not self.__bot_tank_mover.is_running():
            self.__bot_tank_mover.run()
    
    def stop(self):
        self.__bullet_mover.stop()
        self.__bot_tank_mover.stop()

    def __move_bullet(self, bullet:Bullet) -> None:
        collided_objects = self.__map.get_objects_in_area(bullet.next_position_area)
        if bullet in collided_objects: collided_objects.remove(bullet)
        if bullet.creator in collided_objects: collided_objects.remove(bullet.creator)
        if collided_objects:
            self.__map.remove(bullet)
            self.__bullet_mover.remove(bullet)
            collided = collided_objects[0]
            if collided.can_be_destroyed:
                self.__map.remove(collided)
                if isinstance(collided, Tank):
                    if self.__bot_tank_mover.has(collided): self.__bot_tank_mover.remove(collided)
        elif self.__map.is_out_of_limits(bullet.next_position_area):
            self.__map.remove(bullet)
            self.__bullet_mover.remove(bullet)
        else: self.__map.move(bullet)
            
    def __move_tank(self, tank:Tank) -> None:
        next_direction = tank.direction
        decision = 1
        if self.__players[0].tank.row == tank.row or self.__players[0].tank.column == tank.column:
            decision = random.choice([1,0])
        if self.__players[0].tank.row == tank.row:
            next_direction = self.__directions.get(DIRECTION_RIGHT) if self.__players[0].tank.column > tank.column else self.__directions.get(DIRECTION_LEFT)
        elif self.__players[0].tank.column == tank.column:
            next_direction = self.__directions.get(DIRECTION_DOWN) if self.__players[0].tank.row > tank.row else self.__directions.get(DIRECTION_UP)
        else:
            another_directions = list(self.__directions.values())[:]
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
