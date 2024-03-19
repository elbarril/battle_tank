from models.map.MapObject import MapObject

class MapObjectCompound(MapObject):
    def __init__(self, position, size, map_object, object_size):
        super().__init__(position, size)
        self.__objects:list[MapObject] = [map_object(position, object_size) for position in position*size]

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
    