from models.map.objects.PassableMapObjectCompound import PassableMapObjectCompound
from models.map.objects.Tree import Tree
from models.map.MapObjectSize import MapObjectSize
    
class Forest(PassableMapObjectCompound):
    def __init__(self, position, size):
        super().__init__(position, size, Tree, MapObjectSize(2,2))
