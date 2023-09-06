from tkinter import Canvas
from MapObject import MapObject
from MovableMapObject import MovableMapObject
from Constants import MAP_WIDTH, MAP_HEIGHT, MAP_COLOR
from Constants import MIN_X_POSITION, MAX_X_POSITION
from Constants import MIN_Y_POSITION, MAX_Y_POSITION
from Constants import POINT_WEIGHT

class Map(Canvas):
    def __init__(self, master):
        super().__init__(master, width=MAP_WIDTH, height=MAP_HEIGHT, bg=MAP_COLOR)
        self.__object_ids:dict[MapObject,int] = {}
        self.pack()
    
    @property
    def __objects(self) -> dict[int,MapObject]:
        return {id:key for key,id in self.__object_ids.items()}
    
    def get_objects_in_area(self, area:tuple[int]) -> list[MapObject]:
        left, top, right, bottom = (s*POINT_WEIGHT for s in area)
        object_ids = self.find_overlapping(left, top, right, bottom)
        objects = [self.__objects.get(id) for id in object_ids]
        return objects

    def add(self, map_object:MapObject|MovableMapObject):
        position_x = map_object.column*POINT_WEIGHT
        position_y = map_object.row*POINT_WEIGHT
        id = self.create_image(position_x, position_y, image=map_object.image)
        self.__object_ids.setdefault(map_object, id)
    
    def remove(self, map_object:MapObject):
        map_object_id = self.__object_ids.pop(map_object)
        super().delete(map_object_id)
        
    def move(self, map_object:MovableMapObject):
        map_object_id = self.__object_ids.get(map_object)
        super().move(map_object_id, map_object.direction.column*POINT_WEIGHT, map_object.direction.row*POINT_WEIGHT)
        map_object.move()
    
    def is_out_of_limits(self, area:tuple[int]):
        left, top, right, bottom = (s*POINT_WEIGHT for s in area)
        if left < MIN_X_POSITION or top < MIN_Y_POSITION or right > MAX_X_POSITION or bottom > MAX_Y_POSITION: return True
    
    