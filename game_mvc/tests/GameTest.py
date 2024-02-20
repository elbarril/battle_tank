import unittest
from models.Game import Game
import exceptions.player as player_exceptions
import exceptions.bot as bot_exceptions
import exceptions.game as game_exceptions
import exceptions.level as level_exceptions

class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_new_game(self):
        game = Game()
        self.assertEqual(game, self.game)

    def test_new_player(self):
        self.game.remove_players()
        player_1 = self.game.new_player()
        player_2 = self.game.new_player()
        with self.assertRaises(game_exceptions.MaxPlayersExceededException):
            self.game.new_player()
        self.assertNotEqual(player_1, player_2)

    def test_create_tank(self):
        self.game.remove_players()
        with self.assertRaises(game_exceptions.MissingFirstPlayerException):
            self.game.first_player
        self.game.new_player()
        player_1 = self.game.first_player
        self.assertIsNone(player_1.tank)
        player_1.create_tank((0,0))
        self.assertIsNotNone(player_1.tank)
        with self.assertRaises(player_exceptions.PlayerAlreadyHasTankException):
            player_1.create_tank((0,0))
        with self.assertRaises(game_exceptions.MissingSecondPlayerException):
            self.game.second_player
        player_2_tank = self.game.new_player().create_tank((0,0))
        self.assertNotEqual(player_1.tank, player_2_tank)

    def test_load_level(self):
        self.game.remove_players()
        with self.assertRaises(game_exceptions.NoPlayersToPlayLevelException):
            self.game.new_level(1)
        self.game.new_player()
        with self.assertRaises(level_exceptions.WrongOrEmptyLevelNumber):
            self.game.new_level("1")
        with self.assertRaises(level_exceptions.WrongOrEmptyLevelNumber):
            self.game.new_level(100)
        with self.assertRaises(level_exceptions.NonExistentMapLevelNumber):
            self.game.new_level(11)
        level = self.game.new_level(1)
        from models.game.level.LevelNumber import LevelNumber
        self.assertIsInstance(level.number, LevelNumber)
        self.assertIsNone(level.map)
        level.load_map()
        from models.game.level.Map import Map
        self.assertIsInstance(level.map, Map)

    def test_new_bot(self):
        bot_1 = self.game.new_bot()
        bot_2 = self.game.new_bot()
        self.assertNotEqual(bot_1, bot_2)
        self.assertIsNone(bot_1.tank)
        self.assertIsNone(bot_2.tank)
        bot_1.create_tank((0,0))
        with self.assertRaises(bot_exceptions.BotAlreadyHasTankException):
            bot_1.create_tank((0,0))