from model.SingleMapObject import MapObject, SingleMapObject
from model.Position import Position

class MultipleMapObject(MapObject):
    def __init__(self, position:Position, side:int, section_side:int):
        super().__init__(position, side)
        self.__map_objects:list[SingleMapObject] = []

        y_sections = x_sections = side // section_side
        for y in range(y_sections):
            for x in range(x_sections):
                position_x = self.position.x + x * section_side
                position_y = self.position.y + y * section_side
                position = Position(x=position_x, y=position_y)
                map_object = SingleMapObject(position, section_side)
                self.__map_objects.append(map_object)

    @property
    def list(self): return self.__map_objects