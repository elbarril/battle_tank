from models.Game import Game
from views.GameConsoleView import GameConsoleView

game = Game()

game.new_player()
game.new_player()

game.new_level().load_map().create(*tuple(game.players))

game_console_view = GameConsoleView()
game_console_view.show_map(game.level.map)

player_1_tank = game.players.first.tank
player_2_tank = game.players.second.tank

from models.game.level.map.MovableMapObject import MovableMapObject
def move(movable:MovableMapObject, direction):
    next_position = movable.next_position(direction)
    if not game.level.map.is_valid_position(next_position): return
    if game.level.map.collision(next_position): return
    game.level.map.remove_object(movable)
    movable.move(direction)
    game.level.map.add_object(movable)
    game_console_view.show_map(game.level.map)


events = [(key, lambda movable=player.tank,direction=direction:move(movable, direction)) for player in game.players for key,direction in player.movements]

game_console_view.listen_keyboard(events)
game_console_view.loop()