import sys
from models.game.Game import Game
from views.GameConsoleView import GameConsoleView
from views.GameView import GameView
from controller.GameController import GameController

def main(debug=False):
    game = Game()
    view = GameView()
    GameController(game, view).run(debug)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        options = {
            "debug": "-d" in args,
        }
        main(**options)
    else: main()