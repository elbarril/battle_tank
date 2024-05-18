from .. import MapObject
from ...MapPosition import MapPosition
from ..MapObjectSize import MapObjectSize


class CompoundMapObject(MapObject):
    def __init__(self, position, size, map_object: type[MapObject], object_size: MapObjectSize):
        super().__init__(position, size)
        width, height = self.size // object_size
        self.__objects: list[MapObject] = []
        for y in range(height):
            for x in range(width):
                pos_x = self.position.x + object_size.width * x
                pos_y = self.position.y + object_size.height * y
                object = map_object(MapPosition(pos_x, pos_y), object_size)
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
