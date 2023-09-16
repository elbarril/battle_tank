from tkinter import Tk
from Map import Map
from MapObjectMover import MapObjectMover
from Level import Level
from Player import Player
from Direction import Direction

class Game(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(0,0)
        self.__map = Map(self)
        self.__mover = MapObjectMover(self.__map)

    def play(self, level_id) -> None:
        level = Level(level_id)
        level.create_map()
        
        for wall in level.walls:
            for brick in wall.bricks:
                self.__map.add(brick)

        for player in level.players:
            self.__mover.add_player(player)
            self.__bind_player_events(player)

        for bot in level.bots: self.__mover.add_bot(bot.tank)
        
        
        #self.bind("<Escape>", lambda e:self.__reset())

        self.mainloop()

        if self.__mover.is_player_alive and level.has_next: return level.next_level_id
    
    def __bind_player_events(self, player:Player):
        def __move_tank(direction_key:str) -> None:
            next_direction = Direction(player.directions[direction_key])
            if player.tank.direction != next_direction:
                self.__map.remove(player.tank)
                player.tank.rotate(next_direction)
                self.__map.add(player.tank)
            elif not self.__map.is_out_of_limits(player.tank.next_position_area):
                collided_objects = self.__map.get_objects_in_area(player.tank.next_position_area)
                if player.tank in collided_objects: collided_objects.remove(player.tank)
                if not len(collided_objects):
                    self.__map.move(player.tank)
        
        def __tank_shoots() -> None:
            bullet = player.tank.shoot()
            self.__mover.add_bullet(bullet)

        for direction_key in player.directions.keys():
            self.bind(direction_key, lambda e,dk=direction_key:__move_tank(dk))

        for shoot_key in player.shoot_keys:
            self.bind(shoot_key, lambda e:__tank_shoots())
    
    def __reset(self):
        self.__map.delete('all')
        self.quit()
        self.play()
        
    def end(self):
        #self.__mover.stop()
        self.quit()
    