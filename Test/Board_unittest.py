import unittest
import copy
from Main.Model.Board import Board
from Main.Model.Tank import Tank
from Main.Model.MapElement import MapElement
from Main.Model.LevelFactory import LevelFactory
from Main.Model.Constants import (
    LEVELS,
    FIRST_LEVEL,
    PLAYER_SPAWN_DIRECTION,
    PLAYER_SPAWN_SPEED,
    EXCEPTIONS_MESSAGES,
    EXCODE_POOR,
    TEST_OUT_OF_LIMITS_COLUMN,
    TEST_OUT_OF_LIMITS_ROW,
    TEST_VALID_COLUMN,
    TEST_VALID_ROW
)
    
class TestBoard(unittest.TestCase):
    __board:Board = None
    __level_factory:LevelFactory = None
    
    @classmethod
    def setUpClass(cls):
        cls.__board = Board.get_instance()
        cls.__level_factory = LevelFactory.get_instance()

    def test_level_elements_in_board(self):
        first_level = self.__level_factory.first_level
        board_positions = []
        self.__board.add_level_elements(first_level.elements)
        for row in self.__board.positions:
            for position in row:
                board_positions.append(position)
                self.assertIsInstance(position.element, MapElement)
        self.assertEqual(len(first_level.elements), len(board_positions))
        
        first_level_board_positions = copy.deepcopy(self.__board.positions)

        next_level = None
        if self.__level_factory.has_next_level:
            next_level = self.__level_factory.next_level

        if len(LEVELS) > int(FIRST_LEVEL):
            self.__board.add_level_elements(next_level.elements)
            self.assertNotEqual(first_level_board_positions, self.__board.positions)
        else:
            self.assertIsNone(next_level)

    def test_tank_in_board(self):
        with self.assertRaises(Exception) as context:
            tank = Tank(column=TEST_OUT_OF_LIMITS_COLUMN, row=TEST_OUT_OF_LIMITS_ROW, direction=PLAYER_SPAWN_DIRECTION, speed=PLAYER_SPAWN_SPEED)
            self.__board.add_tank(tank)
        self.assertTrue(EXCEPTIONS_MESSAGES[EXCODE_POOR].format(column=TEST_OUT_OF_LIMITS_COLUMN, row=TEST_OUT_OF_LIMITS_ROW) in str(context.exception))

        with self.assertRaises(IndexError) as context:
            tank = Tank(column=TEST_OUT_OF_LIMITS_COLUMN, row=TEST_OUT_OF_LIMITS_ROW, direction=PLAYER_SPAWN_DIRECTION, speed=PLAYER_SPAWN_SPEED)
            self.__board.positions[TEST_OUT_OF_LIMITS_ROW][TEST_OUT_OF_LIMITS_COLUMN].tank = tank

        with self.assertRaises(Exception) as context:
            tank_in_position = self.__board.get_position(TEST_OUT_OF_LIMITS_ROW,TEST_OUT_OF_LIMITS_COLUMN).tank
            self.assertIsNone(tank_in_position)
        self.assertTrue(EXCEPTIONS_MESSAGES[EXCODE_POOR].format(column=TEST_OUT_OF_LIMITS_COLUMN, row=TEST_OUT_OF_LIMITS_ROW) in str(context.exception))
        
        with self.assertRaises(IndexError) as context:
            tank_in_position = self.__board.positions[TEST_OUT_OF_LIMITS_ROW][TEST_OUT_OF_LIMITS_COLUMN].tank
            self.assertIsNone(tank_in_position)

        tank = Tank(column=TEST_VALID_COLUMN, row=TEST_VALID_ROW, direction=PLAYER_SPAWN_DIRECTION, speed=PLAYER_SPAWN_SPEED)
        self.__board.add_tank(tank)
        self.__board.positions[TEST_VALID_ROW][TEST_VALID_COLUMN].tank = tank
        tank_in_position_1, tank_in_position_2 = None, None
        tank_in_position_1 = self.__board.get_position(TEST_VALID_ROW,TEST_VALID_COLUMN).tank
        tank_in_position_2 = self.__board.positions[TEST_VALID_ROW][TEST_VALID_COLUMN].tank

        self.assertIsNotNone(tank_in_position_1)
        self.assertIsNotNone(tank_in_position_2)
        self.assertEqual(tank_in_position_1, tank_in_position_2)
        self.assertEqual(tank_in_position_1, tank)
        self.assertEqual(tank, tank_in_position_2)