from models.Game import Game
from views.GameConsoleView import GameConsoleView

from models.game.map.MovableMapObject import MovableMapObject
from models.game.map.MovableObjectDirection import MovableObjectDirection

from utils.functions import handle_exception

class GameController:
    def __init__(self, model:Game, view:GameConsoleView):
        self.model = model
        self.view = view

    def run(self):
        self.view.listen_keyboard("space", self.__play)
        self.view.listen_keyboard("p", self.__toggle_mode)
        self.view.loop()

    def __toggle_mode(self):
        self.model.toggle_players_mode()
        self.view.show("Mode ", self.model.mode)
    
    def __play(self):
        self.model.new_level()
        self.model.create_players()
        self.__set_players_movement_events()
        self.model.play_level()
        self.view.show_map(self.model.level.map)

    def __set_players_movement_events(self):
        for player in self.model.players:
            for key, direction in player.movements:
                event = lambda m=player.tank,d=direction:self.__move_object(m, d)
                self.view.listen_keyboard(key, event)

    def __move_object(self, movable:MovableMapObject, direction:MovableObjectDirection):
        next_position = movable.position + direction
        map = self.model.level.map
        if not map.is_valid_position(next_position): return
        movable.direction = direction
        if map.collision(next_position): return
        map.remove_object(movable)
        movable.move(next_position)
        map.add_object(movable)
        self.view.show_map(map)