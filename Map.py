from tkinter import Canvas
from MapObject import MapObject
from MovableMapObject import MovableMapObject
from Position import POSITION_WIDTH, POSITION_HEIGHT

MAP_ROWS = 50
MAP_COLUMS = 50

MAP_COLOR = 'gray'

MAP_WIDTH = MAP_COLUMS*POSITION_WIDTH
MAP_HEIGHT = MAP_ROWS*POSITION_HEIGHT

class Map(Canvas):
    def __init__(self, master):
        super().__init__(master, width=MAP_WIDTH, height=MAP_HEIGHT, bg=MAP_COLOR)
        self.__object_ids:dict[MapObject,int] = {}
        self.pack()
    
    @property
    def __objects(self) -> dict[int,MapObject]:
        return {id:key for key,id in self.__object_ids.items()}
    
    def get_objects_in_area(self, area:tuple[int]) -> list[MapObject]:
        left, top, right, bottom = area
        object_ids = self.find_overlapping(left, top, right, bottom)
        objects = [self.__objects.get(id) for id in object_ids]
        return objects

    def add(self, map_object:MapObject):
        id = self.create_image(map_object.position.x, map_object.position.y, image=map_object.image)
        self.__object_ids.setdefault(map_object, id)
        return map_object
    
    def remove(self, map_object:MapObject):
        super().delete(self.__object_ids.get(map_object))
        return map_object
        
    def move(self, map_object:MovableMapObject):
        super().move(self.__object_ids.get(map_object), map_object.direction.x, map_object.direction.y)
        map_object.move()
    
    def is_out_of_limits(self, area:tuple[int]):
        left, top, right, bottom = area
        if left < 0 or top < 0 or right > MAP_WIDTH or bottom > MAP_HEIGHT: return True
    
    