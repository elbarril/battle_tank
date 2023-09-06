from tkinter import Tk
from Map import Map
from BulletMover import BulletMover
from BotMover import BotMover
from Level import Level
from Direction import Direction, DIRECTIONS
from Constants import SHOOT_KEY

FIRST_LEVEL = 1

class Game(Tk):
    __max_bullets_at_same_time = 3
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(0,0)
        self.__level = Level(FIRST_LEVEL)
        self.__map = Map(self)
        self.__bullet_mover = BulletMover(self.__map)
        self.__bot_mover = BotMover(self.__map)

    def play(self) -> None:
        player = self.__level.players[0]
        self.__player_tank = player.tank
        self.__map.add(self.__player_tank)
        
        self.__bot_mover.set_player(player)
        
        for bot in self.__level.bots:
            #self.__map.add(bot.tank)
            self.__bot_mover.add(bot.tank)

        for wall in self.__level.walls:
            for brick in wall.bricks:
                self.__map.add(brick)

        for direction_key in DIRECTIONS.keys():
            self.bind(direction_key, lambda e,dk=direction_key:self.__move_player_tank(dk))

        self.bind(SHOOT_KEY, lambda e:self.__player_shoots())
        
        
        self.bind("<Escape>", lambda e:self.__reset())
        
        self.__bot_mover.run()
        
        self.mainloop()
        
    def __reset(self):
        self.__map.delete("all")
        self.__level = Level(self.__level.key)
        self.play()
    
    def __move_player_tank(self, direction_key:str) -> None:
        next_direction = Direction(direction_key)
        if self.__player_tank.direction != next_direction:
            self.__map.remove(self.__player_tank)
            self.__player_tank.rotate(next_direction)
            self.__map.add(self.__player_tank)
            return
        next_area = self.__player_tank.next_position_area
        if not self.__map.is_out_of_limits(next_area):
            collided_objects = self.__map.get_objects_in_area(next_area)
            if self.__player_tank in collided_objects: collided_objects.remove(self.__player_tank)
            if not len(collided_objects):
                self.__map.move(self.__player_tank)
    
    def __player_shoots(self) -> None:
        if len(self.__bullet_mover.bullets) < self.__max_bullets_at_same_time:
            bullet = self.__player_tank.shoot()
            self.__bullet_mover.add(bullet).run()
