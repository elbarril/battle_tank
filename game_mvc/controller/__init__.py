from models.game import Game
from views import GameView, TK_KEYBOARD

from models.map.MapObject import MapObject
from models.map.MovableMapObject import MovableMapObject
from models.map.MovableObjectDirection import MovableObjectDirection
from models.map.MapPosition import MapPosition
from models.map.objects.PlayerTank import PlayerTank
from models.map.objects.Bullet import Bullet

class GameController:
    def __init__(self, model:Game, view:GameView):
        self.model = model
        self.view = view
        self.__current_binds = []

    def run(self, debug:bool):
        self.__debug = debug
        self.__init_menu()
        self.view.set_mode_label(self.model.mode)
        self.view.mainloop()

    def __init_menu(self):
        self.model.reset()
        self.view.remove_pause_menu()
        self.view.remove_map_canvas()
        self.__unbind_current_binds()
        self.__bind_menu_events()

    def __toggle_mode(self):
        self.model.toggle_players_mode()
        self.view.remove_mode_label()
        self.view.set_mode_label(self.model.mode)
    
    def __play(self):
        self.model.load_players()
        self.model.load_level()
        self.__play_level()

    def __play_level(self):
        self.view.set_map_canvas(self.model.level.map)
        self.__unbind_current_binds()
        self.__bind_level_events()
        self.model.play_level()

    def __pause(self):
        self.view.remove_map_canvas()
        self.view.set_pause_menu()
        self.__unbind_current_binds()
        self.__bind_pause_events()
        self.model.pause_level()

    def __resume(self):
        self.view.remove_pause_menu()
        self.__play_level()

    def __exit(self):
        self.view.focus_set()
        self.view.quit()

    def __bind_menu_events(self):
        bind = self.view.bind(TK_KEYBOARD.ESC, lambda e:self.__exit())
        self.__current_binds.append((TK_KEYBOARD.ESC, bind))
        bind = self.view.bind(TK_KEYBOARD.SPACE, lambda e:self.__play())
        self.__current_binds.append((TK_KEYBOARD.SPACE, bind))
        bind = self.view.bind(TK_KEYBOARD.M, lambda e:self.__toggle_mode())
        self.__current_binds.append((TK_KEYBOARD.M, bind))

    def __bind_level_events(self):
        for player in self.model.players:
            for key, direction in player.movement_keys:
                move = lambda e,m=player.tank,d=direction:self.__move_or_rotate_object(m, d)
                bind = self.view.bind(key, move)
                self.__current_binds.append((key, bind))
            for key in player.shoot_keys:
                shoot = lambda e,t=player.tank:self.__tank_shoots(t)
                bind = self.view.bind(key, shoot)
                self.__current_binds.append((key, bind))
        bind = self.view.bind(TK_KEYBOARD.P, lambda e:self.__pause())
        self.__current_binds.append((TK_KEYBOARD.P, bind))

    def __bind_pause_events(self):
        bind = self.view.bind(TK_KEYBOARD.ESC, lambda e:self.__init_menu())
        self.__current_binds.append((TK_KEYBOARD.ESC, bind))
        bind = self.view.bind(TK_KEYBOARD.P, lambda e:self.__resume())
        self.__current_binds.append((TK_KEYBOARD.P, bind))

    def __unbind_current_binds(self):
        for key,bind in self.__current_binds:
            self.view.unbind(key, funcid=bind)
        self.__current_binds.clear()

    def __tank_shoots(self, tank:PlayerTank):
        bullet = tank.shoot()
        self.__move_bullet(bullet)
        del self.model.level.map[bullet.position*bullet.size]

    def __move_bullet(self, bullet:Bullet):
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
            self.__move_bullet(bullet)
        #self.view.delete_object_view(bullet)

    def __move_or_rotate_object(self, movable:MovableMapObject, direction:MovableObjectDirection):
        map = self.model.level.map
        next_position = movable.position + direction
        if movable.direction != direction or self.__is_valid_position(next_position*movable.size):
            if movable.direction != direction:
                movable.direction = direction
                self.view.update_object_view(movable)
            else:
                if self.__get_collisions(movable, next_position): return
                del map[movable.position*movable.size]
                movable.position = next_position
                map[movable.position*movable.size] = movable
                self.view.move_object_view(movable)

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