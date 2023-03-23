import os
from Main.Model.Game import Game
from Main.Model.Constants import DISPLAY_WIDTH, DISPLAY_HEIGHT
from pygame import display, Surface

class GameView:
    __instance = None
    __screen:Surface = None
    __model:Game = None

    @classmethod
    def get_instance(cls, model:Game):
        if cls.__instance is None:
            cls.initialize(model)
        return cls.__instance

    @classmethod
    def initialize(cls, model:Game):
        cls.__instance = cls()
        cls.__model = model
        cls.__screen = display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    @property
    def model(self) -> Game:
        return self.__model

    @property
    def screen(self) -> Surface:
        return self.__screen

    def show_game_info(self) -> None:
        if self.model.title:
            print(self.model.title.upper(), end="")
            if self.model.time:
                print(" - ", end="")
                print("Time:", str(self.model.time))

    def show_board(self) -> None:
        for row in self.model.board.positions:
            print(str([str(position.tank if position.tank else position.bullet if position.bullet else position.element) for position in row]))

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        
        display.update()

    def refresh(self):
        self.clear_screen()
        self.show_game_info()
        self.show_board()