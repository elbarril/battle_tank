from models.Game import Game
from views.GameConsoleView import GameConsoleView

from models.game.level.map.MovableMapObject import MovableMapObject
from models.game.level.map.MovableMapObjectDirection import MapObjectDirection

class GameController:
    def __init__(self, model:Game, view:GameConsoleView):
        self.model = model
        self.view = view

    def run(self):
        self.model.new_player()
        level = self.model.new_level()
        
        self.view.show_map(level.map)
        events = [(key, lambda movable=player.tank,direction=direction:self.move_object(movable, direction)) for player in self.model.players for key,direction in player.movements]

        self.view.listen_keyboard(events)
        self.view.loop()

    def move_object(self, movable:MovableMapObject, direction):
        if not isinstance(movable, MovableMapObject):
            raise Exception(f"Object {movable} cannot move.")
        if not isinstance(direction, MapObjectDirection):
            raise Exception("Wrong direction.")
        next_position = movable.position + direction
        map = self.model.level.map
        if not map.is_valid_position(next_position): return
        movable.direction = direction
        if map.collision(next_position): return
        map.remove_object(movable)
        movable.move(next_position)
        map.add_object(movable)
        self.view.show_map(map)