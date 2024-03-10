from models.map.objects.Tank import Tank

class BotTank(Tank):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.symbol = "B"
        self.image = 'bottank'

    def __str__(self):
        return super().__str__()