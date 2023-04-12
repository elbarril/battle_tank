class Controller:
    def __init__(self):
        from model.Game import Game
        from view.GameView import GameView

        self.__game:Game = Game.get_instance()
        self.__view:GameView = GameView.get_instance(self.__game)

    def run_game(self) -> None:
        while self.__game.level_factory.has_next_level:
            self.__game.load_next_level()
            while self.__game.player.has_lifes:
                self.__game.play_level()
                self.__view.refresh()
            break
