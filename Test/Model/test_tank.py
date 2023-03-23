import unittest
from Main.Model.Tank import Tank

class TestTank(unittest.TestCase):

    def testGeneral(self):
        tank = Tank()
        self.assertEqual(tank.isWorking(), True)

if __name__ == '__main__':
    unittest.main()        
