from models.map.objects.Tank import Tank

class BotTank(Tank):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = "B"
        self.image = 'bottank'

    def __str__(self):
        return super().__str__()