from models import Game
from views import GameView, TK_KEYBOARD

from models.map.object import MapObjectDirection
from models.map.object.abstract import SolidMapObject
from models.map.object.tank import Bullet

from models.player import AbstractPlayer

from .GameBindManager import GameBindManager

from log import log_time_elapsed

import time

class GameController:
    def __init__(self, model:Game, view:GameView):
        self.model = model
        self.view = view
        self.binds = GameBindManager(view)

        self.__bullets:list[Bullet] = []

    def run(self):
        self.__init_menu()
        self.view.set_mode_label(self.model.mode)
        self.view.mainloop()

    def __init_menu(self):
        self.model.reset()
        self.view.remove_pause_label()
        self.view.remove_map_canvas()
        self.binds.clear()
        self.binds.add(TK_KEYBOARD.ESC, lambda e:self.__exit())
        self.binds.add(TK_KEYBOARD.SPACE, lambda e:self.__play())
        self.binds.add(TK_KEYBOARD.M, lambda e:self.__toggle_mode())

    def __toggle_mode(self):
        self.model.toggle_players_mode()
        self.view.remove_mode_label()
        self.view.set_mode_label(self.model.mode)

    def __play(self):
        self.model.load_players()
        self.model.load_level()
        self.model.load_map()
        self.__play_level()

    def __play_level(self):
        self.view.set_map_canvas(self.model.level.map)
        self.binds.clear()
        for player in self.model.players:
            for movement in player.movements:
                move = lambda e,p=player,d=movement.direction:self.__player_moves(p, d)
                self.binds.add(movement.key, move)
            for shooting in player.shooting:
                self.binds.add(shooting.key, lambda e,p=player:self.__player_shoots(p))
        self.binds.add(TK_KEYBOARD.P, lambda e:self.__pause())
        self.model.play_level()

    def __pause(self):
        self.view.remove_map_canvas()
        self.view.set_pause_label()
        self.binds.clear()
        self.binds.add(TK_KEYBOARD.ESC, lambda e:self.__init_menu())
        self.binds.add(TK_KEYBOARD.P, lambda e:self.__resume())
        self.model.pause_level()

    def __resume(self):
        self.view.remove_pause_label()
        self.__play_level()

    def __exit(self):
        self.view.focus_set()
        self.view.quit()

    def __player_shoots(self, player:AbstractPlayer):
        if player.tank.shooting: return
        bullet = player.tank.shoot()
        player.tank.shooting = True
        map = self.model.level.map
        bullet_positions = bullet.position*bullet.size

        if not bullet_positions in map: return
        other_objects = [object for object in map[bullet_positions] if object and not object is bullet and isinstance(object, SolidMapObject)]

        if other_objects:
            for object in other_objects:
                del map[object.position * object.size]
                self.view.delete_object_view(object)
            bullet.tank.shooting = False
        else:
            self.view.create_object_view(bullet)
            map[bullet_positions] = bullet
            self.__bullets.append(bullet)
        self.bullets_move()

    def bullets_move(self):
        map = self.model.level.map
        time.sleep(.05)
        for bullet in self.__bullets:
            bullet_positions = bullet.position*bullet.size
            del map[bullet_positions]
            bullet.position = bullet.position + bullet.direction
            bullet_positions = bullet.position * bullet.size
            self.view.move_object_view(bullet)

            if not bullet_positions in map:
                self.__bullets.remove(bullet)
                self.view.delete_object_view(bullet)
                bullet.tank.shooting = False
                break
            other_objects = [object for object in map[bullet_positions] if object and not object is bullet and isinstance(object, SolidMapObject)]

            if other_objects:
                for object in other_objects:
                    del map[object.position * object.size]
                    self.view.delete_object_view(object)
                self.__bullets.remove(bullet)
                self.view.delete_object_view(bullet)
                bullet.tank.shooting = False
                break
            
            map[bullet_positions] = bullet

        if self.__bullets: self.bullets_move()

    def __player_moves(self, player:AbstractPlayer, direction:MapObjectDirection):
        map = self.model.level.map
        tank = player.tank

        if tank.direction != direction:
            tank.direction = direction
            return self.view.update_object_view(tank)

        next_position = tank.position + direction
        next_positions = next_position * tank.size

        if next_positions in map:
            other_objects = [object for object in map[next_positions] if object and not object is tank and isinstance(object, SolidMapObject)]
            if other_objects: return
            del map[tank.position*tank.size]
            tank.position = next_position
            map[next_positions] = tank
            return self.view.move_object_view(tank)