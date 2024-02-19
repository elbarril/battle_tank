from models.game.player.Bot import Bot
from models.game.collections.PlayerCollection import PlayerCollection

class BotCollection(PlayerCollection):
    def add(self, bot):
        return super().add(bot)
    
    def __next__(self) -> Bot:
        return super().__next__()
    
    def __getitem__(self, index) -> Bot:
        return super().__getitem__(index)