from tkinter import Label, Tk, Canvas, PhotoImage, NW
from typing import Callable
from views.ViewInterfaz import ViewInterfaz
from models.map.MapObject import MapObject
from models.map.MapObjectCompound import MapObjectCompound
from models.map.MovableMapObject import MovableMapObject
from constants.map import MAP_WIDTH, MAP_HEIGHT, MAP_ROW_POSITIONS, MAP_COLUMN_POSITIONS, PIXEL_FACTOR

class GameView(Tk, ViewInterfaz):
    __enable_images = True
    __enable_colors = True
    __KEYBOARD = {
        "space": "<space>",
        "esc": "<Escape>",
        "m": "m",
        "up": "<Up>",
        "down": "<Down>",
        "right": "<Right>",
        "left": "<Left>",
        "w": "w",
        "a": "a",
        "s": "s",
        "d": "d"
    }
        
    def __init__(self):
        Tk.__init__(self)
        ViewInterfaz.__init__(self, self.__KEYBOARD)
        self.mode_label = Label(self, text="")
        self.mode_label.pack()
        x0, y0, x1, y1 = self.__get_pixel_coords(MAP_WIDTH, MAP_HEIGHT)
        self.canvas = Canvas(self, width=x0, height=y0)
        self.canvas.pack(expand=True)
        self.images:dict[str, PhotoImage] = {}
        self.__canvas_objects = dict()

    def set_mode_label(self, *args):
        self.mode_label.config(text=" ".join((str(arg) for arg in args)))

    def show(self, *args):
        pass

    def show_map(self, map):
        pass

    def create_object_view(self, object):
        if not isinstance(object, MapObject):
            raise TypeError(f"Wrong object type: {object}")
        if isinstance(object, MapObjectCompound):
            for obj in object:
                self.create_object_view(obj)
        elif not object in self.__canvas_objects:
            object_view = None
            x0, y0, x1, y1 = self.__get_pixel_coords(object.position.x, object.position.y, object.size.width, object.size.height)
            if object.image and self.__enable_images:
                if not isinstance(object.image, str):
                    raise TypeError(f"Wrong object image type: {object.image}")
                image = self.__get_object_image(object)
                object_view = self.canvas.create_image(x0, y0, image=image, anchor=NW)
            elif object.color and self.__enable_colors:
                if not isinstance(object.color, str):
                    raise TypeError(f"Wrong object color type: {object.color}")
                object_view = self.canvas.create_rectangle(x0, y0, x1, y1, fill=object.color)
            self.__canvas_objects.setdefault(object, object_view)

    def delete_object_view(self, object):
        if not isinstance(object, MapObject):
            raise TypeError(f"Wrong object type: {object}")
        if object in self.__canvas_objects:
            object_view = self.__canvas_objects.get(object)
            self.canvas.delete(object_view)

    def update_object_view(self, object):
        if not isinstance(object, MapObject):
            raise TypeError(f"Wrong object type: {object}")
        if object in self.__canvas_objects:
            object_view = self.__canvas_objects.get(object)
            if object.image and self.__enable_images:
                image = self.__get_object_image(object)
                self.canvas.itemconfig(object_view, image=image)
            elif object.color and self.__enable_colors:
                self.canvas.itemconfig(object_view, fill=object.color)

    def move_object_view(self, object):
        if not isinstance(object, MovableMapObject):
            raise TypeError(f"Wrong object type: {object}")
        if object in self.__canvas_objects:
            object_view = self.__canvas_objects.get(object)
            x0,y0,x1,y1 = self.__get_pixel_coords(object.direction.x*object.velocity, object.direction.y*object.velocity)
            self.canvas.move(object_view, x0, y0)

    def __get_object_image(self, object):
        if not isinstance(object, MapObject):
            raise TypeError(f"Wrong object type: {object}")
        if not isinstance(object.image, str):
            raise TypeError(f"Wrong object image type: {object.image}")
        if isinstance(object, MovableMapObject):
            image_path = 'images\/' + object.image + '_' + str(object.direction) + '.png'
        else:
            image_path = 'images\/' + object.image + '.png'
        if image_path in self.images:
            return self.images[image_path]
        else:
            image = PhotoImage(file=image_path)
            image = image.subsample(MAP_COLUMN_POSITIONS//object.size.width, MAP_ROW_POSITIONS//object.size.height)
            return self.images.setdefault(image_path, image)

    def __get_pixel_coords(self, x, y, width=None, height=None):
        if not (isinstance(x,(int,float)) and isinstance(y,(int,float))):
            raise TypeError(f"Wrong number type\n x:{x}, y:{y}")
        x0 = x1 = x * MAP_ROW_POSITIONS * PIXEL_FACTOR
        y0 = y1 = y * MAP_COLUMN_POSITIONS * PIXEL_FACTOR
        if width and height:
            if not (isinstance(width,int) and isinstance(height,int)):
                raise TypeError(f"Wrong number type\n width:{width}, height:{height}")
            x1 = x0 + width * MAP_ROW_POSITIONS * PIXEL_FACTOR
            y1 = y0 + height * MAP_COLUMN_POSITIONS * PIXEL_FACTOR
        return (x0, y0, x1, y1)

    def listen_keyboard(self, key, event):
        if not isinstance(key,str):
            raise TypeError(f"Wrong key type {key}")
        if not isinstance(event, Callable):
            raise TypeError(f"Wrong event type {event}")
        self.bind(self._get_key(key), lambda e:event())

    def shut_keyboard(self, key):
        if not isinstance(key,str):
            raise TypeError(f"Wrong key type {key}")
        if key in self.__KEYBOARD:
            self.unbind(self.__KEYBOARD[key])

    def loop(self, exit_key):
        if not isinstance(exit_key,str):
            raise TypeError(f"Wrong key type {exit_key}")
        self.bind(self._get_key(exit_key), lambda e:self.__exit())
        self.mainloop()

    def __exit(self):
        self.focus_set()
        self.quit()