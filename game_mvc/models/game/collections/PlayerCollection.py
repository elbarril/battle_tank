from models.game.player.AbstractPlayer import AbstractPlayer
from utils.Collection import Collection
from exceptions.player import *
from exceptions.game import *

class PlayerCollection(Collection):
    def add(self, player):
        if not isinstance(player, AbstractPlayer):
            raise NotPlayerInstanceException()
        super().add(player)
        return player
    
    @property
    def first(self):
        if not len(self):
            raise MissingFirstPlayerException()
        return self[0]
    
    @property
    def second(self):
        if not len(self) > 1:
            raise MissingSecondPlayerException()
        return self[1]
    
    def __tuple__(self):
        return tuple(self)
    
    def __next__(self) -> AbstractPlayer:
        return super().__next__()
    
    def __getitem__(self, index) -> AbstractPlayer:
        return super().__getitem__(index)