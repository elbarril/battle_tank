from models.Game import Game
from views.GameConsoleView import GameConsoleView

from models.game.level.map.MovableMapObject import MovableMapObject
from models.game.level.map.MovableMapObjectDirection import MapObjectDirection

from utils.functions import handle_exception

class GameController:
    def __init__(self, model:Game, view:GameConsoleView):
        self.model = model
        self.view = view

    def run(self):
        self.model.create_players()
        level = self.model.new_level()
        self.model.play_level()
        self.set_players_movement_events()
        self.view.show_map(level.map)
        self.view.loop()

    def set_players_movement_events(self):
        for player in self.model.players:
            for key, direction in player.movements:
                event = lambda m=player.tank,d=direction:self.move_object(m, d)
                self.view.listen_keyboard(key, event)

    def move_object(self, movable:MovableMapObject, direction:MapObjectDirection):
        next_position = movable.position + direction
        map = self.model.level.map
        if not map.is_valid_position(next_position): return
        movable.direction = direction
        if map.collision(next_position): return
        map.remove_object(movable)
        movable.move(next_position)
        map.add_object(movable)
        self.view.show_map(map)