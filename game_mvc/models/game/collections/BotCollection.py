from models.game.collections.AbstractPlayerCollection import AbstractPlayerCollection
from models.game.player.Bot import Bot

class BotCollection(AbstractPlayerCollection):
    def __next__(self) -> Bot:
        return super().__next__()
    
    def __getitem__(self, index) -> Bot:
        return super().__getitem__(index)