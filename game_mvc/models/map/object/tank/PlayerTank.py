from .Tank import Tank
from .Bullet import Bullet

class PlayerTank(Tank):
    def __init__(self, player_number, position, size):
        super().__init__(position, size)
        self.player_number = player_number
        self.symbol = "P"
        self.shooting = False

    def shoot(self):
        return Bullet(self)

class PlayerOneTank(PlayerTank):
    def __init__(self, position, size):
        super().__init__(1, position, size)
        self.symbol = "1"
        self.image = 'playertank'

class PlayerTwoTank(PlayerTank):
    def __init__(self, position, size):
        super().__init__(2, position, size)
        self.symbol = "2"
        self.image = 'playertank2'