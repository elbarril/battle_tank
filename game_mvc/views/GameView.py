from tkinter import Label, Tk, Canvas, PhotoImage
from tkinter.constants import *

from models.map.Map import Map
from models.map.MapObject import MapObject
from models.map.MapObjectCompound import MapObjectCompound
from models.map.MovableMapObject import MovableMapObject
from constants.map import MAP_WIDTH, MAP_HEIGHT, MAP_ROW_POSITIONS, MAP_COLUMN_POSITIONS, PIXEL_FACTOR

class TK_KEYBOARD:
    SPACE = "<space>"
    ESC = "<Escape>"
    M = "m"
    UP = "<Up>"
    DOWN = "<Down>"
    RIGHT = "<Right>"
    LEFT = "<Left>"
    W = "w"
    A = "a"
    S = "s"
    D = "d"
    P = 'p'

class GameView(Tk):
    __enable_images = True
    __enable_colors = True

    images:dict[str, PhotoImage] = {}    
    canvas_objects:dict[MapObject, int] = {}
    
    def __init__(self):
        Tk.__init__(self)
        self.canvas = None
        self.mode_label = None
        self.pause_menu = None

    def set_mode_label(self, mode):
        self.mode_label = Label(self, text="Mode: %d players." % mode)
        self.mode_label.pack()

    def remove_mode_label(self):
        if self.mode_label: self.mode_label.destroy()

    def set_pause_menu(self):
        self.pause_menu = Label(self, text='<P> to resume\n<Esc> to back to menu')
        self.pause_menu.pack()

    def remove_pause_menu(self):
        if self.pause_menu: self.pause_menu.destroy()

    def set_map_canvas(self, map:Map):
        self.canvas = Canvas(self)
        x0, y0 = self.__get_pixel_coords(map.width, map.height)
        self.canvas.config(width=map.width, height=map.height)
        self.canvas.pack(expand=True)

        for row in map:
            for object in row: self.create_object_view(object)

    def remove_map_canvas(self):
        if self.canvas: self.canvas.destroy()
        self.canvas_objects.clear()

    def create_object_view(self, object:MapObject):
        if isinstance(object, MapObjectCompound):
            for obj in object:
                self.create_object_view(obj)
        elif not object in self.canvas_objects:
            object_view = self.__get_object_view(object)
            self.canvas_objects.setdefault(object, object_view)
        else: self.update_object_view(object)

    def delete_object_view(self, object:MapObject):
        if self.canvas_objects.get(object):
            object_view = self.canvas_objects.get(object)
            self.canvas.delete(object_view)

    def update_object_view(self, object:MapObject):
        if self.canvas_objects.get(object):
            object_view = self.canvas_objects.get(object)
            if object.image and self.__enable_images:
                image = self.__get_object_image(object)
                self.canvas.itemconfig(object_view, image=image)
            elif object.color and self.__enable_colors:
                self.canvas.itemconfig(object_view, fill=object.color)

    def move_object_view(self, object:MovableMapObject):
        if object in self.canvas_objects:
            object_view = self.canvas_objects.get(object)
            x0, y0 = self.__get_pixel_coords(object.direction.x, object.direction.y)
            self.canvas.move(object_view, x0, y0)

    def __get_object_view(self, object:MapObject):
        object_view = None
        x0, y0, x1, y1 = self.__get_pixel_coords(object.position.x, object.position.y, object.size.width, object.size.height)
        if object.image and self.__enable_images:
            image = self.__get_object_image(object)
            object_view = self.canvas.create_image(x0, y0, image=image, anchor=NW)
        elif object.color and self.__enable_colors:
            object_view = self.canvas.create_rectangle(x0, y0, x1, y1, fill=object.color)
        return object_view

    def __get_object_image(self, object:MapObject):
        if object.image in self.images:
            return self.images[object.image]
        else:
            image = PhotoImage(file='images/' + object.image + '.png')
            image = image.subsample(MAP_COLUMN_POSITIONS//object.size.width, MAP_ROW_POSITIONS//object.size.height)
            return self.images.setdefault(object.image, image)

    def __get_pixel_coords(self, x, y, width=None, height=None):
        x0 = x * MAP_ROW_POSITIONS * PIXEL_FACTOR
        y0 = y * MAP_COLUMN_POSITIONS * PIXEL_FACTOR
        if width and height:
            x1 = x0 + width * MAP_ROW_POSITIONS * PIXEL_FACTOR
            y1 = y0 + height * MAP_COLUMN_POSITIONS * PIXEL_FACTOR
            return (x0, y0, x1, y1)
        return (x0, y0)