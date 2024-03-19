from models.map.MapObjectCompound import MapObjectCompound
from models.map.objects.SolidMapObject import SolidMapObject
    
class SolidMapObjectCompound(MapObjectCompound, SolidMapObject):
    def __init__(self, position, size, map_object, object_size):
        super().__init__(position, size, map_object, object_size)

    def __str__(self):
        return super().__str__()