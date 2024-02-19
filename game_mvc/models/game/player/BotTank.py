from models.game.player.Tank import Tank

class BotTank(Tank):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = "B"
