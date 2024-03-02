from tkinter import Label, Tk, Canvas, PhotoImage
from views.ViewInterfaz import ViewInterfaz
from models.map.Map import Map
from constants.map import MAP_POSITION_WIDTH, MAP_POSITION_HEIGHT, PIXEL_FACTOR

class GameView(Tk, ViewInterfaz):
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

    def show_map(self, map:Map):
        if self.canvas: self.canvas.destroy()
        self.canvas = Canvas(self, width=map.width*PIXEL_FACTOR*MAP_POSITION_WIDTH, height=map.height*PIXEL_FACTOR*MAP_POSITION_HEIGHT)
        objects = []
        for y,row in enumerate(map):
            for x,object in enumerate(row):
                if not object in objects:
                    objects.append(object)
                    if object.is_compound:
                        for obj in object: self.__add_object_to_canvas(obj, obj.position[0].x, obj.position[0].y)

                    else: self.__add_object_to_canvas(object, x, y)
        self.canvas.pack(expand=True)

    def __add_object_to_canvas(self, object, x, y):
        x0 = x * MAP_POSITION_WIDTH * PIXEL_FACTOR
        y0 = y * MAP_POSITION_HEIGHT * PIXEL_FACTOR
        x1 = x0 + object.size.width * MAP_POSITION_WIDTH * PIXEL_FACTOR
        y1 = y0 + object.size.height * MAP_POSITION_HEIGHT * PIXEL_FACTOR
        if object.image:
            image_path = 'images\/' + object.image + ('_' + str(object.direction) + '.png' if object.is_movable else '.png')
            if image_path in self.images:
                image = self.images[image_path]
            else:
                image = PhotoImage(file=image_path)
                self.images.setdefault(image_path, image)
            self.canvas.create_image(x0, y0, image=image, anchor='nw')

    def listen_keyboard(self, key, event):
        self.bind(self._get_key(key), lambda e:event())

    def shut_keyboard(self, key):
        self.unbind(self._get_key(key))

    def loop(self, exit_key):
        self.bind(self._get_key(exit_key), lambda e:self.__exit())
        self.mainloop()

    def __exit(self):
        self.focus_set()
        self.quit()