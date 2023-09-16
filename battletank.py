from Game import Game
from Constants import FIRST_LEVEL

game = Game()

next_level = game.play(FIRST_LEVEL)

while next_level:
    next_level = game.play(next_level)

game.end()