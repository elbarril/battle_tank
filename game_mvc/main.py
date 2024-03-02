import sys
from models.game.Game import Game
from views.GameConsoleView import GameConsoleView
from views.GameView import GameView
from controller.GameController import GameController

def main(view):
    game = Game()
    GameController(game, view).run()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--console":
        view = GameConsoleView()
    else:
        view = GameView()
    
    main(view)