import unittest
from tests.GameTest import GameTest

test_loader = unittest.TestLoader()

test_suite = unittest.TestSuite()
test_suite.addTest(test_loader.loadTestsFromTestCase(GameTest))

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_suite)