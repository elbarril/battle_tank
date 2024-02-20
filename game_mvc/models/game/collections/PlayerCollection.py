from models.game.collections.AbstractPlayerCollection import AbstractPlayerCollection
from models.game.player.Player import Player

class PlayerCollection(AbstractPlayerCollection):
    def __next__(self) -> Player:
        return super().__next__()
    
    def __getitem__(self, index) -> Player:
        return super().__getitem__(index)