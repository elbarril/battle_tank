from models.map.MapObject import MapObject
from models.map.MapObjectSize import MapObjectSize

class MapObjectCompound(MapObject):
    __objects:list[MapObject] = []
    
    def __init__(self, position, size, map_object, object_size=MapObjectSize(1,1)):
        super().__init__(position, size)
        for position in self.position:
            object = map_object(position, object_size)
            self.__objects.append(object)

    def __setitem__(self, index, object):
        self.__objects[index] = object

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.__objects[index]
        elif isinstance(index, MapObject):
            return self.__objects.index(index)
        else:
            raise TypeError(f"Wrong index or value type: {index}")

    def __iter__(self):
        return iter(self.__objects)
    