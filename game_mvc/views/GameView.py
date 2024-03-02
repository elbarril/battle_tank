from tkinter import Label, Tk, Canvas
from views.ViewInterfaz import ViewInterfaz
from models.map.Map import Map
from constants.map import MAP_POSITION_WIDTH, MAP_POSITION_HEIGHT

PIXEL_FACTOR = 5

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

    def show(self, *args):
        if self.mode_label: self.mode_label.destroy()
        self.mode_label = Label(self, text=" ".join((str(arg) for arg in args)))
        self.mode_label.pack()

    def show_map(self, map:Map):
        if self.canvas: self.canvas.destroy()
        self.canvas = Canvas(self, width=map.width*PIXEL_FACTOR*MAP_POSITION_WIDTH, height=map.height*PIXEL_FACTOR*MAP_POSITION_HEIGHT)
        for y,row in enumerate(map):
            for x,object in enumerate(row):
                x0 = x*object.size.width*PIXEL_FACTOR
                y0 = y*object.size.height*PIXEL_FACTOR
                x1 = x0+object.size.width*PIXEL_FACTOR
                y1 = y0+object.size.height*PIXEL_FACTOR
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=object.color, outline=object.color)
        self.canvas.pack(expand=True)

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