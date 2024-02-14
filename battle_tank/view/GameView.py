from tkinter import Tk
from model.Game import Game
from threading import Thread
from view.MapView import MapView, MapObjectView
from view.TankView import TankView, BulletView, Image
import time

from constants import (
    MAP_COLOR,
    MAP_OBJECTS,
    DIRECTIONS,
    DIRECTION_KEYS,
    PLAYER_IMAGE_FILENAME,
    BULLET_IMAGE_FILENAME,
    DIRECTION_IMAGE_SUFFIX
)

class GameView(Tk):
    def __init__(self, model:Game):
        super().__init__()
        self.__fullscreen = True
        self.__model = model
        self.attributes("-fullscreen", self.__fullscreen)

        self.__map_view = MapView(self, model.map, MAP_COLOR)
        self.__bullets:list[BulletView] = []
        self.__bullet_mover:Thread = None

        self.__player_tank_images = {DIR:Image(PLAYER_IMAGE_FILENAME+DIRECTION_IMAGE_SUFFIX[DIR]) for DIR in DIRECTIONS.values()}
        self.__bullets_images = {DIR:Image(BULLET_IMAGE_FILENAME+DIRECTION_IMAGE_SUFFIX[DIR]) for DIR in DIRECTIONS.values()}
        self.__map_object_images = {MAP_OBJECT:MAP_OBJECT for MAP_OBJECT in MAP_OBJECTS}

    def start(self):
        for map_object in self.__model.level.map_objects:
            continue
            map_object_view = MapObjectView(map_object, self.__map_object_images[map_object.code])
            self.__map_view.create()

        for player in self.__model.players:
            tank = TankView(player.tank, self.__player_tank_images, self.__bullets_images)
            self.__map_view.create(tank)
            for direction_key in DIRECTION_KEYS: self.bind(direction_key, lambda e,t=tank,dk=direction_key:self.move_tank(t,DIRECTIONS[dk]))
            self.bind("<space>", lambda e,t=tank:self.tank_shoots(t))

        self.bind("<Escape>", lambda e,window=self:self.end(window))
        self.bind("f", lambda e,window=self:self.toggle_fullscreen(window))
        #self.__model.bot.play()
        self.mainloop()
        
    def move_tank(self, tank:TankView, direction:str):
        collided_objects = self.__map_view.get_collided_objects_by_area(tank.next_area(direction))
        if tank.model in collided_objects: collided_objects.remove(tank.model)
        print(collided_objects)
        if len(collided_objects): return
        self.__map_view.move(tank, direction)
            
    def tank_shoots(self, tank:TankView) -> None:
        bullet = tank.shoot()
        self.__bullets.append(bullet)
        self.__map_view.create(bullet)
        if not self.__bullet_mover or not self.__bullet_mover.is_alive():
            self.__bullet_mover = Thread(target=self.__move_bullets)
            self.__bullet_mover.daemon = True
            self.__bullet_mover.start()
    
    def __move_bullets(self):
        while len(self.__bullets):
            for bullet in self.__bullets:
                self.__move_bullet(bullet)
            time.sleep(.05)
    
    def __move_bullet(self, bullet:BulletView):
        collided_objects = self.__map_view.get_collided_objects_by_area(bullet.next_area(bullet.model.direction))
        if len(collided_objects):
            self.__remove_map_object(bullet)
            self.__remove_map_object(collided_objects[0])
        else: self.__map_view.move(bullet)
    
    def __remove_map_object(self, map_object):
        self.__map_view.remove(map_object)
        if isinstance(map_object, TankView):
            player_tanks = [player.tank for player in self.__model.players]
            if map_object.model in player_tanks:
                self.__model.players.remove(player_tanks.index(map_object.model))
                if not len(self.__model.players): self.end(self)
            else: self.__model.bot.remove_tank(map_object.model)
        elif isinstance(map_object, BulletView):
            self.__bullets.remove(map_object)

    def end(self, game:Tk):
        if self.__fullscreen: game.attributes("-fullscreen", False)
        game.quit()

    def toggle_fullscreen(self, game:Tk):
        self.__fullscreen = False if self.__fullscreen else True
        game.attributes("-fullscreen", self.__fullscreen)