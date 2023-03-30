import unittest
from model.Game import Game

class TestGame(unittest.TestCase):
    def test_create_game(self):
        game = Game.get_instance()
        game2 = Game.get_instance()
        self.assertEqual(game, game2)