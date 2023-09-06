from tkinter import Tk
from Map import Map
from MapObjectMover import MapObjectMover
from Level import Level
from Direction import Direction, DIRECTIONS
from Constants import FIRST_LEVEL, SHOOT_KEY

class Game(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(0,0)
        self.__map = Map(self)
        self.__mover = MapObjectMover(self.__map)

    def play(self, level_id=FIRST_LEVEL) -> None:
        level = Level(level_id)
        self.__player_one, self.__player_two = level.players
        self.__mover.add_player_tank(self.__player_one.tank)
        self.__map.add(self.__player_one.tank)
        
        for wall in level.walls:
            for brick in wall.bricks:
                self.__map.add(brick)
        
        for bot in level.bots: self.__mover.add_tank(bot.tank)
        
        self.__bind_player_one_events()
        
        self.mainloop()
    
    def __bind_player_one_events(self):
        def __player_one_tank_move(direction_key:str) -> None:
            next_direction = Direction(direction_key)
            if self.__player_one.tank.direction != next_direction:
                self.__map.remove(self.__player_one.tank)
                self.__player_one.tank.rotate(next_direction)
                self.__map.add(self.__player_one.tank)
                return
            next_area = self.__player_one.tank.next_position_area
            if not self.__map.is_out_of_limits(next_area):
                collided_objects = self.__map.get_objects_in_area(next_area)
                if self.__player_one.tank in collided_objects: collided_objects.remove(self.__player_one.tank)
                if not len(collided_objects):
                    self.__map.move(self.__player_one.tank)
                
            self.__map.update()
        
        def __player_one_tank_shoots() -> None:
            bullet = self.__player_one.tank.shoot()
            self.__mover.add_bullet(bullet)
            self.__map.update()

        def __reset():
            self.__map.delete('all')
            self.quit()
            self.play()
        
        for direction_key in DIRECTIONS.keys():
            self.bind(direction_key, lambda e,dk=direction_key:__player_one_tank_move(dk))

        self.bind(SHOOT_KEY, lambda e:__player_one_tank_shoots())

        self.bind("<Escape>", lambda e:__reset())