import unittest
from models.game.Game import Game

class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_new_game(self):
        game = Game()
        self.assertEqual(game, self.game)