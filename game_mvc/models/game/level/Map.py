from models.game.level.map.MapSize import MapSize
from models.game.level.map.MapObject import MapObject
from models.game.level.map.MapObjectType import MapObjectType
from models.game.level.map.MapObjectPosition import MapObjectPosition
from models.game.level.map.MapMatrix import MapMatrix, MapMatrixRow
from models.game.level.map.factories.MapObjectFactory import MapObjectFactory

class Map(MapMatrix):
    def __init__(self, map_size:MapSize=MapSize()):
        super().__init__(map_size.height)
        self.__size = map_size

    def add_row(self):
        self.add(MapMatrixRow(self.__size.width))

    def is_valid_position(self, position:MapObjectPosition):
        if not isinstance(position, MapObjectPosition):
            raise Exception()
        return position.x >=0 and position.y >= 0 and position.y < len(self) and position.x < len(self[position.y])
    
    def collision(self, position:MapObjectPosition):
        if not isinstance(position, MapObjectPosition):
            raise Exception()
        return self[position.y][position.x].is_solid
    
    def remove_object(self, object:MapObject):
        if not isinstance(object, MapObject):
            raise Exception()
        self[object.position.y][object.position.x] = MapObjectFactory.create(MapObjectType.FLUID, object.position.x, object.position.y)

    def add_object(self, object:MapObject):
        if not isinstance(object, MapObject):
            raise Exception()
        self[object.position.y][object.position.x] = object