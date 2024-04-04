import sys
from models import Game
from views import GameView
from controller import GameController

def main(debug=False):
    game = Game()
    view = GameView()
    GameController(game, view).run(debug)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        options = {
            "debug": "-d" in args or "--debug" in args,
        }
        main(**options)
    else: main()