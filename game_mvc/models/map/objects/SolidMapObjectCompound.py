from models.map.MapObjectCompound import MapObjectCompound
from models.map.objects.SolidMapObject import SolidMapObject
    
class SolidMapObjectCompound(MapObjectCompound):
    def __init__(self, position, map_object=SolidMapObject):
        super().__init__(position, map_object)
        self.is_solid = True