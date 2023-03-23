import unittest
import Test.Board_unittest as Board_test
import Test.Game_unittest as Game_test

if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = [
        loader.loadTestsFromModule(Board_test),
        loader.loadTestsFromModule(Game_test)
    ]
    suite = unittest.TestSuite()
    suite.addTests(tests)
    
    runner = unittest.TextTestRunner(verbosity=3)
    results = runner.run(suite)