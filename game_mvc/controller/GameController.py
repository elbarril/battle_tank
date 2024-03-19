from models.game.Game import Game
from views.GameConsoleView import GameConsoleView

from models.map.MapObject import MapObject
from models.map.MovableMapObject import MovableMapObject
from models.map.MovableObjectDirection import MovableObjectDirection
from models.map.MapPosition import MapPosition
from models.map.objects.Tank import Tank
from models.map.objects.SolidMapObject import SolidMapObject
from models.map.objects.FluidMapObject import FluidMapObject

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
        self.model.load_players()
        self.model.load_level()
        self.model.load_map()
        
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
        map[bullet.position] = bullet
        while False:
            collisions = self.__get_collisions(bullet, bullet.position)
            if collisions or not map.is_valid_position(bullet.position):
                break
            map[bullet.position] = FluidMapObject(bullet.position, bullet.size)
            bullet.position = bullet.position + bullet.direction
            map[bullet.position] = bullet
            self.view.show_map(map)

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
        map = self.model.level.map
        next_position = movable.position + direction
        if movable.direction != direction or self.__object_can_move(movable, next_position):
            if movable.direction != direction:
                movable.direction = direction
            else:
                collisions = self.__get_collisions(movable, next_position)
                if not collisions:
                    for position in movable.position*movable.size:
                        map[position] = FluidMapObject(movable.position, movable.size)
                    movable.position = next_position
                    for position in movable.position*movable.size:
                        map[position] = movable
                else:
                    tanks = [object for object in collisions if isinstance(object, Tank)]
                    if tanks:
                        for position in movable.position*movable.size:
                            map[position] = FluidMapObject(movable.position, movable.size)

            self.view.show_map(map)

    def __object_can_move(self, movable, position):
        if not isinstance(movable, MovableMapObject):
            raise TypeError(f"Wrong movable type: {movable}")
        if not isinstance(position, MapPosition):
            raise TypeError(f"Wrong position type: {position}")
        for pos in position*movable.size:
            if not self.model.level.map.is_valid_position(pos):
                return False
        return True

    def __get_collisions(self, object, position):
        if not isinstance(object, MapObject):
            raise TypeError(f"Wrong object type: {object}")
        if not isinstance(position, MapPosition):
            raise TypeError(f"Wrong position type: {position}")
        return [map_object for map_object in [self.model.level.map[pos] for pos in position*object.size] if map_object != object and isinstance(map_object,SolidMapObject)]
