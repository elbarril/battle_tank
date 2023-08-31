from tkinter import Tk
from Map import Map
from Mover import Mover
from Level import Level
from Keyboard import *
from Direction import Direction, DIRECTIONS

FIRST_LEVEL = 1

class Game(Tk):
    __max_bullets_at_same_time = 3
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(0,0)
        self.__level = Level(FIRST_LEVEL)
        self.__map = Map(self)
        self.__bullet_mover = Mover(self.__map)
        self.__tank_mover = Mover(self.__map)

    def run(self) -> None:
        self.__player = self.__level.player
        self.__map.add(self.__player.tank)

        for obstacle in self.__level.obstacles:
            self.__map.add(obstacle)

        for direction_key in DIRECTIONS.keys():
            self.bind(direction_key, lambda e,dk=direction_key:self.__move_player_tank(dk))

        self.bind(SHOOT_KEY, lambda e:self.__player_shoots())
        
        self.mainloop()
    
    def __move_player_tank(self, direction_key:str) -> None:
        self.__player.tank.direction = Direction(direction_key)
        if self.__map.can_move(self.__player.tank):
            self.__map.move(self.__player.tank)
    
    def __player_shoots(self) -> None:
        if len(self.__bullet_mover.objects) < self.__max_bullets_at_same_time:
            bullet = self.__player.tank.shoot()
            self.__bullet_mover.add(bullet)
