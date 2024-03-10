from models.map.objects.Tank import Tank

class PlayerTank(Tank):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.symbol = "P"
        self.image = 'playertank'