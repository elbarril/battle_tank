from tkinter import Label, Tk, Canvas, PhotoImage
from typing import Callable
from views.ViewInterfaz import ViewInterfaz
from models.map.Map import Map
from models.map.MapObject import MapObject
from models.map.MapObjectCompound import MapObjectCompound
from models.map.MovableMapObject import MovableMapObject
from utils.Size import Size
from constants.map import MAP_POSITION_WIDTH, MAP_POSITION_HEIGHT, PIXEL_FACTOR

class GameView(Tk, ViewInterfaz):
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
        self.canvas = None
        self.mode_label = None
        self.images:dict[str, PhotoImage] = {}

    def show(self, *args):
        if self.mode_label: self.mode_label.destroy()
        self.mode_label = Label(self, text=" ".join((str(arg) for arg in args)))
        self.mode_label.pack()

    def show_map(self, map):
        if not isinstance(map, Map):
            raise TypeError(f"Wrong map type: {map}")
        if self.canvas: self.canvas.destroy()
        x0, y0, x1, y1 = self.__get_pixel_coords(0, 0, map.size)
        self.canvas = Canvas(self, width=x1, height=y1)
        canvas_objects = set()
        for y,row in enumerate(map):
            for x,object in enumerate(row):
                if object in canvas_objects: continue
                self.__add_object_to_canvas(object, x, y)
                canvas_objects.add(object)
        self.canvas.pack(expand=True)

    def __add_object_to_canvas(self, object, x, y):
        if not (isinstance(x,int) and isinstance(y,int)):
            raise TypeError(f"Wrong number type\n x:{x}, y:{y}")
        if not isinstance(object, MapObject):
            raise TypeError(f"Wrong object type: {object}")
        if isinstance(object, MapObjectCompound):
            for obj in object:
                for pos in obj.position:
                    self.__add_object_to_canvas(obj, pos.x, pos.y)
        else:
            x0, y0, x1, y1 = self.__get_pixel_coords(x, y, object.size)
            if object.image:
                image = self.__get_object_image(object)
                self.canvas.create_image(x0, y0, image=image, anchor='nw')
            elif self.__enable_colors:
                if not isinstance(object.color, str):
                    raise TypeError(f"Wrong object color type: {object.color}")
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=object.color)

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
            return self.images.setdefault(image_path, image)

    def __get_pixel_coords(self, x, y, size=None):
        if not (isinstance(x,int) and isinstance(y,int)):
            raise TypeError(f"Wrong number type\n x:{x}, y:{y}")
        x0 = x1 = x * MAP_POSITION_WIDTH * PIXEL_FACTOR
        y0 = y1 = y * MAP_POSITION_HEIGHT * PIXEL_FACTOR
        if size:
            if not isinstance(size, Size):
                raise TypeError(f"Wrong size type: {size}")
            x1 = x0 + size.width * MAP_POSITION_WIDTH * PIXEL_FACTOR
            y1 = y0 + size.height * MAP_POSITION_HEIGHT * PIXEL_FACTOR
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