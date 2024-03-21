from models.game.Game import Game
from views.GameView import GameView

from models.map.MapObject import MapObject
from models.map.MovableMapObject import MovableMapObject
from models.map.MovableObjectDirection import MovableObjectDirection
from models.map.MapPosition import MapPosition
from models.map.objects.Tank import Tank
from models.map.objects.SolidMapObject import SolidMapObject
from models.map.objects.FluidMapObject import FluidMapObject

from time import sleep

class GameController:
    def __init__(self, model:Game, view:GameView):
        self.model = model
        self.view = view

    def run(self):
        self.view.listen_keyboard("space", self.__play)
        self.view.listen_keyboard("m", self.__toggle_mode)
        self.view.set_mode_label("Mode:", self.model.mode, "players")
        self.view.loop("esc")

    def __toggle_mode(self):
        self.model.toggle_players_mode()
        self.view.set_mode_label("Mode:", self.model.mode, "players")
    
    def __play(self):
        self.view.shut_keyboard("space")
        self.view.shut_keyboard("m")
        self.model.load_players()
        self.model.load_level()
        self.model.load_map()
        
        self.__set_players_movement_events()
        self.__set_players_shoot_events()
        self.model.play_level()

        for row in self.model.level.map:
            for object in row:
                self.view.create_object_view(object)

    def __set_players_shoot_events(self):
        for player in self.model.players:
            for key in player.shoot:
                shoot = lambda t=player.tank:self.__tank_shoots(t)
                self.view.listen_keyboard(key, shoot)

    def __tank_shoots(self, tank):
        if not isinstance(tank, Tank):
            raise TypeError(f"Wrong tank type: {tank}")      
        map = self.model.level.map
        bullet = tank.shoot()
        map[bullet.position] = bullet
        next_position = bullet.position + bullet.direction
        self.view.create_object_view(bullet)
        while True:
            if not map.is_valid_position(next_position*bullet.size): break
            map[bullet.position*bullet.size] = FluidMapObject(bullet.position, bullet.size)
            collisions = self.__get_collisions(bullet, next_position)
            if collisions:
                for object in collisions:
                    map[object.position*object.size] = FluidMapObject(object.position, object.size)
                    self.view.delete_object_view(object)
                    if not isinstance(object, Tank): break
                break
            else:
                bullet.position = next_position
                map[bullet.position*bullet.size] = bullet
                next_position = bullet.position + bullet.direction
                self.view.move_object_view(bullet)
        self.view.delete_object_view(bullet)

    def __set_players_movement_events(self):
        for player in self.model.players:
            for key, direction in player.movements:
                move = lambda m=player.tank,d=direction:self.__move_or_rotate_object(m, d)
                self.view.listen_keyboard(key, move)

    def __move_or_rotate_object(self, movable, direction):
        if not isinstance(movable, MovableMapObject):
            raise TypeError(f"Wrong movable type: {movable}")
        if not isinstance(direction, MovableObjectDirection):
            raise TypeError(f"Wrong direction type: {direction}")
        map = self.model.level.map
        next_position = movable.position + direction
        if movable.direction != direction or map.is_valid_position(next_position*movable.size):
            if movable.direction != direction:
                movable.direction = direction
                self.view.update_object_view(movable)
            else:
                collisions = self.__get_collisions(movable, next_position)
                if not collisions:
                    map[movable.position*movable.size] = FluidMapObject(movable.position, movable.size)
                    movable.position = next_position
                    map[movable.position*movable.size] = movable
                    self.view.move_object_view(movable)
                else:
                    return
                    tanks = [object for object in collisions if isinstance(object, Tank)]
                    if tanks:
                        map[movable.position*movable.size] = FluidMapObject(movable.position, movable.size)


    def __get_collisions(self, object, position):
        if not isinstance(object, MapObject):
            raise TypeError(f"Wrong object type: {object}")
        if not isinstance(position, MapPosition):
            raise TypeError(f"Wrong position type: {position}")
        return [map_object for map_object in self.model.level.map[position*object.size] if map_object != object and isinstance(map_object, SolidMapObject)]
