from utils.Collection import Collection

from models.game.level.map.MapObject import MapObject

class MapMatrixRow(Collection):
    def __init__(self, map_width:int):
        super().__init__(map_width)

    def add(self, object):
        return super().add(object)
    
    def __setitem__(self, index, object):
        super().__setitem__(index,object)
    
    def __getitem__(self, index) -> MapObject:
        return super().__getitem__(index)
    
    def __next__(self) -> MapObject:
        return super().__next__()

class MapMatrix(Collection):
    def __init__(self, height:int):
        super().__init__(height)

    def add(self, row):
        return super().add(row)
    
    def __getitem__(self, index) -> MapMatrixRow:
        return super().__getitem__(index)
    
    def __next__(self) -> MapMatrixRow:
        return super().__next__()
    