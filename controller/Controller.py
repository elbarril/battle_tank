from controller.PyGame import PyGame

class Controller(PyGame):
    def __init__(self):
        from model.Game import Game
        from view.GameView import GameView
        super().__init__()
        self.__game:Game = Game.get_instance()
        self.__view:GameView = GameView.get_instance(self.__game)

    def run_game(self) -> None:
        while self.__game.level_factory.has_next_level and self.__game.player.has_lifes:
            self.__game.load_next_level()
            while self.__game.player.has_lifes and self.__game.has_bots:
                self.__view.refresh()
                self.__game.play_level()
            
            self.__view.refresh()
