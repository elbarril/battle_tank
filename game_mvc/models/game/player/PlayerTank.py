from models.game.player.Tank import Tank

class PlayerTank(Tank):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = "P"