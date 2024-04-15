from models.game import Game
from views import GameView, TK_KEYBOARD

from models.map.MapObject import MapObject
from models.map.objects.SolidMapObject import SolidMapObject
from models.map.MapObjectDirection import MapObjectDirection
from models.map.MapPosition import MapPosition
from models.map.objects.PlayerTank import PlayerTank
from models.map.objects.Bullet import Bullet
from models.player import AbstractPlayer

class GameBind:
    def __init__(self, key:str, id:str) -> None:
        self.__key = key
        self.__id = id

    @property
    def key(self) -> str:
        return self.__key
    
    @property
    def id(self) -> str:
        return self.__id
    
    def __eq__(self, other):
        if isinstance(other, GameBind):
            return self.key == other.key and self.id == other.id

from typing import Callable

class GameBindManager:
    def __init__(self, view:GameView) -> None:
        self.__view = view
        self.__binds:list[GameBind] = []

    def add(self, key:str, callable:Callable) -> None:
        id = self.__view.bind(key, callable)
        self.__binds.append(GameBind(key, id))

    def remove(self, bind:GameBind) -> None:
        self.__view.unbind(bind.key, bind.id)
        self.__binds.remove(bind)

    def clear(self) -> None:
        for bind in self:
            self.remove(bind)

    def __iter__(self) -> list[GameBind]:
        return iter(self.__binds)

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
        self.view.remove_pause_menu()
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
        self.view.set_pause_menu()
        self.binds.clear()
        self.binds.add(TK_KEYBOARD.ESC, lambda e:self.__init_menu())
        self.binds.add(TK_KEYBOARD.P, lambda e:self.__resume())
        self.model.pause_level()

    def __resume(self):
        self.view.remove_pause_menu()
        self.__play_level()

    def __exit(self):
        self.view.focus_set()
        self.view.quit()

    def __player_shoots(self, player:AbstractPlayer):
        bullet = player.tank.shoot()
        self.__bullets.append(bullet)
        while self.__bullets and False:
            for b in self.__bullets:
                self.__bullet_moves(b)
        del self.model.level.map[bullet.position*bullet.size]

    def __bullet_moves(self, bullet:Bullet):
        if self.__is_valid_position(bullet.position):
            map = self.model.level.map
            collisions = self.__get_collisions(bullet, bullet.position)
            if collisions:
                for object in collisions:
                    del map[object.position*object.size]
                    self.view.delete_object_view(object)
                return
            map[bullet.position*bullet.size] = bullet
            self.view.create_object_view(bullet)
            bullet.position = bullet.position + bullet.direction
            self.view.move_object_view(bullet)
            self.__bullet_moves(bullet)
        self.__bullets.remove(bullet)
        self.view.delete_object_view(bullet)

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

    def __get_collisions(self, object:MapObject, position:MapPosition) -> list[MapObject]:
        return [map_object for map_object in self.model.level.map[position*object.size] if map_object and map_object != object]

    def __is_valid_position(self, position):
        if not isinstance(position, MapPosition) and not isinstance(position, list):
            raise TypeError(f"Wrong position type: {position}")
        if isinstance(position, list):
            for pos in position:
                if not self.__is_valid_position(pos):
                    return False
            return True
        else:
            return position.x >= 0 and position.y >= 0 and position.y < self.model.level.map.height and position.x < self.model.level.map.width