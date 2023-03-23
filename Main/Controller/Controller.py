from Main.Model.Game import Game
from Main.View.GameView import GameView
from Main.Controller.PyGame import PyGame
import sys
import time
from typing import Literal

class Controller(PyGame):
    def __init__(self):
        super().__init__()
        self.__game = Game.get_instance()
        self.__view = GameView.get_instance(self.__game)

    @property
    def game(self) -> Game:
        return self.__game
    
    @property
    def view(self) -> GameView:
        return self.__view

    def run_game(self) -> None:
        self.game.start()
        self.view.show_game_info()
        self.view.show_board()

        while True:
            self.__player_actions()
            self.__move_bullets()

            self.__update_game()
            time.sleep(.3)

    def __player_actions(self) -> None:
        for event in self.events:
            if event.type == self.event_type_quit:
                self.quit()

            elif event.type == self.event_type_key_pressed:
                key_pressed = self.get_key_pressed(event)
                direction:Literal["up", "down", "left", "right"] = None

                if key_pressed in self.moving_keys:
                    if key_pressed == self.key_up:
                        direction = "up" 

                    elif key_pressed == self.key_down:
                        direction = "down"

                    elif key_pressed == self.key_left:
                        direction = "left"

                    elif key_pressed == self.key_right:
                        direction = "right"

                    self.game.player_tank.direction = direction

                    if not self.game.board.detect_collision(self.game.player_tank):
                        self.game.player_tank.move()

                elif key_pressed == self.key_space:
                    bullet = self.game.player_tank.shoot()
                    self.game.board.bullets.append(bullet)

    def __move_bullets(self):
        for bullet in self.game.board.bullets:
            if not self.game.board.detect_collision(bullet):
                bullet.move()

            else:
                self.game.board.remove_bullet(bullet)

    def __update_game(self):
        self.game.update()
        self.view.refresh()

    def quit(self):
        super().quit()
        sys.exit()