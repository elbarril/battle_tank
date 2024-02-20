from abc import ABC
from models.game.player.AbstractPlayer import AbstractPlayer
from utils.Collection import Collection
from exceptions.player import *
from exceptions.game import *

class AbstractPlayerCollection(Collection, ABC):
    def add(self, player):
        if not isinstance(player, AbstractPlayer):
            raise NotPlayerInstanceException()
        super().add(player)
        return player
    
    def __tuple__(self):
        return tuple(self)
    
    def __next__(self) -> AbstractPlayer:
        return super().__next__()
    
    def __getitem__(self, index) -> AbstractPlayer:
        return super().__getitem__(index)