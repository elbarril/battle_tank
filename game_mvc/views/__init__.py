from tkinter import Label, Tk, Canvas, PhotoImage
from tkinter import constants as tkconst

from models.map import Map

from models.map.object import MapObject

from models.map.object.abstract import CompoundMapObject
from models.map.object.abstract import MovableMapObject

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

    __images:dict[str, PhotoImage] = {}    
    __canvas_objects:dict[MapObject, int] = {}
    
    def __init__(self):
        Tk.__init__(self)
        self.__canvas = None
        self.__mode_label = None
        self.__pause_label = None
        self.__fullscreen = True

        self.attributes("-fullscreen", self.__fullscreen)
        self.bind("f", lambda e:self.__toggle_fullsreen())

    def __toggle_fullsreen(self):
        self.__fullscreen = not self.__fullscreen
        self.attributes("-fullscreen", self.__fullscreen)

    def set_mode_label(self, mode):
        self.__mode_label = Label(self, text="Mode: %d players." % mode)
        self.__mode_label.pack()
        self.update()

    def remove_mode_label(self):
        if self.__mode_label: self.__mode_label.destroy()
        self.update()

    def set_pause_label(self):
        self.__pause_label = Label(self, text='<P> to resume\n<Esc> to back to menu\n<F> toggle fullscreen')
        self.__pause_label.pack()
        self.update()

    def remove_pause_label(self):
        if self.__pause_label: self.__pause_label.destroy()
        self.update()

    def set_map_canvas(self, map:Map):
        self.__canvas = Canvas(self, bg=map.background_color)
        x0, y0 = self.__get_pixel_coords(map.width, map.height)
        self.__canvas.config(width=x0, height=y0)
        self.__canvas.pack(expand=True)

        for row in map:
            for object in row: 
                if object is not None: self.create_object_view(object)

        for layer in sorted(map.layers):
            self.__canvas.lift(layer)
        self.update()

    def remove_map_canvas(self):
        if self.__canvas: self.__canvas.destroy()
        self.__canvas_objects.clear()
        self.update()

    def create_object_view(self, object:MapObject):
        if isinstance(object, CompoundMapObject):
            for obj in object:
                self.create_object_view(obj)
        elif not object in self.__canvas_objects:
            x0, y0, x1, y1 = self.__get_pixel_coords(object.position.x, object.position.y, object.size.width, object.size.height)
            if object.image and self.__enable_images:
                image = self.__get_object_image(object)
                object_view = self.__canvas.create_image(x0, y0, image=image, anchor=tkconst.NW, tags=[object.layer])
            elif object.color and self.__enable_colors:
                object_view = self.__canvas.create_rectangle(x0, y0, x1, y1, fill=object.color, tags=[object.layer])
            self.__canvas_objects.setdefault(object, object_view)
        else: self.update_object_view(object)
        self.update()

    def delete_object_view(self, object:MapObject):
        object_view = self.__canvas_objects.get(object)
        if object_view:
            self.__canvas_objects.pop(object)
            self.__canvas.delete(object_view)
            self.update()

    def update_object_view(self, object:MapObject):
        object_view = self.__canvas_objects.get(object)
        if object_view:
            if object.image and self.__enable_images:
                image = self.__get_object_image(object)
                self.__canvas.itemconfig(object_view, image=image)
            elif object.color and self.__enable_colors:
                self.__canvas.itemconfig(object_view, fill=object.color)
        self.update()

    def move_object_view(self, object:MovableMapObject):
        object_view = self.__canvas_objects.get(object)
        if object_view:
            x0, y0 = self.__get_pixel_coords(object.direction.x, object.direction.y)
            self.__canvas.move(object_view, x0, y0)
        self.update()

    def __get_object_image(self, object:MapObject):
        if object.image in self.__images:
            return self.__images[object.image]
        else:
            image = PhotoImage(file='images/' + object.image + '.png')
            image = image.subsample(4//object.size.width, 4//object.size.height)
            return self.__images.setdefault(object.image, image)

    def __get_pixel_coords(self, x, y, width=None, height=None):
        x0 = x * 10
        y0 = y * 10
        if width and height:
            x1 = x0 + width * 10
            y1 = y0 + height * 10
            return (x0, y0, x1, y1)
        return (x0, y0)