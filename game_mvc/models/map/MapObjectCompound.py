from models.map.MapObject import MapObject

class MapObjectCompound(MapObject):
    def __init__(self, position, map_object):
        super().__init__(position)
        self.is_compound = True
        self.__objects = [map_object(position, self.size / len(self.position)) for position in self.position]

    def __iter__(self):
        return iter(self.__objects)
    