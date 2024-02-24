from models.Game import Game
from views.GameConsoleView import GameConsoleView
from controller.GameController import GameController

game = Game()
game_console_view = GameConsoleView()

GameController(game, game_console_view).run()