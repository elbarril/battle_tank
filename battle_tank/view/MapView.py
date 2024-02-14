from tkinter import Canvas, Tk
from model.Map import Map
from view.MovableSingleMapObjectView import MovableSingleMapObjectView
from view.MapObjectView import MapObjectView, MapObject

class MapView(Canvas):
    def __init__(self, window:Tk, model:Map, color):
        super().__init__(window, width=model.width, height=model.height, bg=color)
        self.pack()
        self.__model = model
        self.__map_objects:dict[int,MapObject] = {}

    def create(self, map_object:MapObjectView) -> MapObjectView:
        for object in map_object.model.list:
            map_x = object.position.x + object.radio
            map_y = object.position.y + object.radio
            object.id = self.create_image(map_x, map_y, image=map_object.image)
            self.__map_objects.setdefault(object.id, object)
        self.update()
        return map_object
    
    def move(self, map_object:MovableSingleMapObjectView, direction) -> None:
        if not self.__model.is_out_of_limits(map_object.next_area(direction)): map_object.move(direction)
        self.coords(map_object.model.id, map_object.model.position.x + map_object.model.radio, map_object.model.position.y + map_object.model.radio)
        self.update()

    def remove(self, map_object:MapObjectView) -> None:
        self.delete(map_object.model.id)
        self.__map_objects.pop(map_object.model.id)
        self.update()

    def get_collided_objects_by_area(self, area:tuple[int,int,int,int]) -> list[MapObject]:
        left, top, right, bottom = area
        map_object_ids = list(self.find_overlapping(left, top, right, bottom))
        map_objects = [object for id in map_object_ids for object in self.__map_objects.get(id).list]
        map_objects = [self.__map_objects.get(id) for id in map_object_ids]
        return map_objects