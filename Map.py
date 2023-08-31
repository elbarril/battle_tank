from tkinter import Canvas
from MapObject import MapObject
from MovableMapObject import MovableMapObject

MAP_ROWS = 50
MAP_COLUMS = 50

POSITION_WIDTH = POSITION_HEIGHT = 10

MAP_COLOR = 'gray'

MAP_WIDTH = MAP_COLUMS*POSITION_WIDTH
MAP_HEIGHT = MAP_ROWS*POSITION_HEIGHT

class Map(Canvas):
    def __init__(self, master):
        super().__init__(master, width=MAP_WIDTH, height=MAP_HEIGHT, bg=MAP_COLOR)
        self.__objects:dict[MapObject,int] = {}
        
        self.pack()

    def __get_next_position_boundries(self, map_object:MovableMapObject) -> tuple[int]:
        
        next_row = map_object.position.row + map_object.direction.row
        next_column = map_object.position.column + map_object.direction.column
        
        half_width = map_object.size.width/2*POSITION_WIDTH
        half_height = map_object.size.height/2*POSITION_WIDTH
        
        left = next_column*POSITION_WIDTH - half_width
        right = next_column*POSITION_WIDTH + half_width
        top = next_row*POSITION_HEIGHT - half_height
        bottom = next_row*POSITION_HEIGHT + half_height
        
        return (left, top, right, bottom)
    
    def can_move(self, map_object:MovableMapObject):
        obj_id = self.__objects.get(map_object)
        if not obj_id:return
        left, top, right, bottom = self.__get_next_position_boundries(map_object)
        if left < 0 or top < 0 or right > MAP_WIDTH or bottom > MAP_HEIGHT: return
        return True

    def get_collided_object(self, map_object:MovableMapObject) -> MapObject:
        obj_id = self.__objects.get(map_object)
        if not obj_id:return
        left, top, right, bottom = self.__get_next_position_boundries(map_object)    
        objects = self.find_overlapping(left, top, right, bottom)
        obj_keys = {id:key for key,id in self.__objects.items()}
        objects_ids = [id for id in objects if id != obj_id]
        if len(objects):
            collided_object = obj_keys[objects_ids[0]]
            map_object_creator = getattr(map_object, 'creator')
            if map_object_creator and map_object_creator == collided_object:return
            return obj_keys[objects_ids[0]]
        
    def add(self, map_object:MapObject):
        y = map_object.position.row * POSITION_HEIGHT
        x = map_object.position.column * POSITION_WIDTH
        id = self.create_image(x, y, image=map_object.image)
        self.__objects.setdefault(map_object, id)
    
    def remove(self, map_object:MapObject):
        obj_id = self.__objects.get(map_object)
        if not obj_id:return
        super().delete(obj_id)
        
    def move(self, map_object:MovableMapObject):
        super().move(self.__objects.get(map_object), map_object.direction.column*POSITION_WIDTH, map_object.direction.row*POSITION_HEIGHT)
        map_object.move()