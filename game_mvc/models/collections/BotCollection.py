from utils.Collection import Collection
from models.player.Bot import Bot

class BotCollection(Collection):
    def add(self, bot):
        return super().add(bot)

    def __next__(self) -> Bot:
        return super().__next__()
    
    def __getitem__(self, index) -> Bot:
        return super().__getitem__(index)