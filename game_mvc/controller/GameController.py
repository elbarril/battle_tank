from models.game.Game import Game
from views.GameConsoleView import GameConsoleView

from models.map.MovableMapObject import MovableMapObject
from models.map.MovableObjectDirection import MovableObjectDirection
from models.map.MapObjectPosition import MapObjectPosition
from models.map.objects.Tank import Tank
from models.map.objects.SolidMapObject import SolidMapObject

from utils.functions import handle_exception

class GameController:
    def __init__(self, model:Game, view:GameConsoleView):
        self.model = model
        self.view = view

    def run(self):
        self.view.listen_keyboard("space", self.__play)
        self.view.listen_keyboard("m", self.__toggle_mode)
        self.view.show("Mode:", self.model.mode, "players")
        self.view.loop("esc")

    def __toggle_mode(self):
        self.model.toggle_players_mode()
        self.view.show("Mode:", self.model.mode, "players")
    
    def __play(self):
        self.view.shut_keyboard("space")
        self.view.shut_keyboard("m")
        self.model.new_level()
        self.model.create_players()
        self.__set_players_movement_events()
        self.__set_players_shoot_events()
        self.model.play_level()
        self.view.show_map(self.model.level.map)

    def __set_players_shoot_events(self):
        for player in self.model.players:
            for key in player.shoot:
                event = lambda t=player.tank:self.__tank_shoots(t)
                self.view.listen_keyboard(key, event)

    def __tank_shoots(self, tank):
        if not isinstance(tank, Tank):
            raise TypeError(f"Wrong tank type: {tank}")      
        map = self.model.level.map
        bullet = tank.shoot()
        moved = self.__move_object(bullet, bullet.direction)
        if moved: self.view.show_map(map)

    def __set_players_movement_events(self):
        for player in self.model.players:
            for key, direction in player.movements:
                event = lambda m=player.tank,d=direction:self.__move_or_rotate_object(m, d)
                self.view.listen_keyboard(key, event)

    def __move_or_rotate_object(self, movable, direction):
        if not isinstance(movable, MovableMapObject):
            raise TypeError(f"Wrong movable type: {movable}")
        if not isinstance(direction, MovableObjectDirection):
            raise TypeError(f"Wrong direction type: {direction}")

        rotated = moved = self.__rotate_object(movable, direction)
        if not rotated:
            moved = self.__move_object(movable, direction)
        if moved:
            self.view.show_map(self.model.level.map)

    def __move_object(self, movable, direction):
        if not isinstance(movable, MovableMapObject):
            raise TypeError(f"Wrong movable type: {movable}")
        if not isinstance(direction, MovableObjectDirection):
            raise TypeError(f"Wrong direction type: {direction}")
        next_position = movable.position + direction
        map = self.model.level.map
        if not map.is_valid_position(next_position): return
        del map[movable]
        collisions = self.__get_collisions(movable, next_position)
        if collisions: return
        movable.position = next_position
        map[movable.position] = movable
        return True

    def __rotate_object(self, movable, direction):
        if not isinstance(movable, MovableMapObject):
            raise TypeError(f"Wrong movable type: {movable}")
        if not isinstance(direction, MovableObjectDirection):
            raise TypeError(f"Wrong direction type: {direction}")
        if movable.direction != direction:
            map = self.model.level.map
            del map[movable]
            movable.direction = direction
            map[movable.position] = movable
            return True

    def __get_collisions(self, object, position):
        if not isinstance(position, MapObjectPosition):
            raise TypeError(f"Wrong position type: {position}")
        return [map_object for map_object in self.model.level.map[position] if map_object != object and isinstance(map_object,SolidMapObject)]
