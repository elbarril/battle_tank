from models.map.objects.Tank import Tank

class PlayerTank(Tank):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.symbol = "P"
        self.image = 'playertank'

class PlayerOneTank(PlayerTank):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.symbol = "1"

class PlayerTwoTank(PlayerTank):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.symbol = "2"