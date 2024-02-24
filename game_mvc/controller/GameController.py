from models.Game import Game
from views.GameConsoleView import GameConsoleView

from models.game.level.map.MovableMapObject import MovableMapObject

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
        next_position = movable.next_position(direction)
        if not self.model.level.map.is_valid_position(next_position) and self.model.level.map.collision(next_position): return
        self.model.level.map.remove_object(movable)
        movable.move(direction)
        self.model.level.map.add_object(movable)
        self.view.show_map(self.model.level.map)