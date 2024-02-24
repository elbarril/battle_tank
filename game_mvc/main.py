from models.Game import Game
from views.GameConsoleView import GameConsoleView

game = Game()

game.new_player()

map = game.new_level().map

game_console_view = GameConsoleView()
game_console_view.show_map(map)

from models.game.level.map.MovableMapObject import MovableMapObject
def move(movable:MovableMapObject, direction):
    next_position = movable.next_position(direction)
    if not map.is_valid_position(next_position) and map.collision(next_position): return
    map.remove_object(movable)
    movable.move(direction)
    map.add_object(movable)
    game_console_view.show_map(map)


events = [(key, lambda movable=player.tank,direction=direction:move(movable, direction)) for player in game.players for key,direction in player.movements]

game_console_view.listen_keyboard(events)
game_console_view.loop()