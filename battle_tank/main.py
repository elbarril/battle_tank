from model.Game import Game
from view.GameView import GameView

game = Game().load()

game_view = GameView(game)

game_view.start()