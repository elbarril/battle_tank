from .Tank import Tank
from .Bullet import Bullet

class BotTank(Tank):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.symbol = "B"
        self.image = 'bottank'

    def shoot(self):
        return Bullet(self)

    def __str__(self):
        return super().__str__()