from tkinter import constants as tkconst
from tkinter import Label, Tk, Canvas, PhotoImage, Frame

from utils.Observable import Observer
from models.GameStateManager import GameState


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
    F = 'f'


class MapObjectView:
    def __init__(self, map_view, id):
        self.__id = id
        self.__map_view = map_view

    def rotate(self, image, color, width, height):
        self.__map_view.update_object(self.__id, image, color, width, height)

    def delete(self):
        self.__map_view.delete_object(self.__id)

    def move(self, move_x, move_y):
        self.__map_view.move_object(self.__id, move_x, move_y)


class MapView(Canvas):
    __enable_images = True

    def __init__(self, game_view, width, height, bg, **kwargs):
        x, y = self.__get_pixel_coords(width, height)
        super().__init__(game_view, width=x, height=y, bg=bg, **kwargs)
        self.pack(expand=True)
        self.__game_view = game_view

    def lift_layers(self, layers: list[str]):
        for layer in sorted(layers):
            self.lift(layer)

    def create_object(self, x, y, width, height, image, color, layer):
        x0, y0, x1, y1 = self.__get_pixel_coords(x, y, width, height)
        if self.__enable_images:
            image = self.__game_view.get_image(
                image) or self.__game_view.create_image(image, width, height)
            id = self.create_image(x0, y0, image=image, layer=layer)
        else:
            id = self.create_rectangle(x0, y0, x1, y1, color, layer=layer)
        self.update()
        object_view = MapObjectView(self, id)
        return object_view

    def create_image(self, x, y, image, anchor=tkconst.NW, layer=None):
        return super().create_image(x, y, image=image, anchor=anchor, tags=[layer])

    def create_rectangle(self, x0, y0, x1, y1, color, layer):
        return super().create_rectangle(x0, y0,  x1, y1, color=color, tags=[layer])

    def delete_object(self, id):
        self.delete(id)
        self.update()

    def update_object(self, id, image, color, width, height):
        if self.__enable_images:
            image = self.__game_view.get_image(
                image) or self.__game_view.create_image(image, width, height)
            self.itemconfig(id, image=image)
        else:
            self.itemconfig(id, fill=color)
        self.update()

    def move_object(self, id, move_x, move_y):
        x0, y0 = self.__get_pixel_coords(move_x, move_y)
        self.move(id, x0, y0)
        self.update()

    def __get_pixel_coords(self, x, y, width=None, height=None):
        x0 = x * 10
        y0 = y * 10
        if width and height:
            x1 = x0 + width * 10
            y1 = y0 + height * 10
            return (x0, y0, x1, y1)
        return (x0, y0)


class PauseFrame(Frame):
    def __init__(self, game_view):
        super().__init__(game_view)
        self.__text = Label(self, text="PAUSE", relief="ridge", fg="red")
        self.__text.pack()
        self.place(x=0, y=0)
        game_view.update()
        frame_x = game_view.winfo_width() // 2 - self.__text.winfo_width() // 2
        frame_y = game_view.winfo_height() // 2 - self.__text.winfo_height() // 2
        self.place(x=frame_x, y=frame_y)


class MenuFrame(Frame, Observer):
    def __init__(self, game_view, modes, mode_selected, selector_image="playertank_right"):
        Frame.__init__(self, game_view)
        Observer.__init__(self)
        self.pack()
        self.__game_view = game_view
        self.__mode_selector = {}
        self.__selector_image = self.__game_view.get_image(
            selector_image) or self.__game_view.create_image(selector_image, 4, 4)
        mode_frame = Frame(self)
        mode_frame.pack(side="right", expand=True, fill="both")
        selector_frame = Frame(self)
        selector_frame.pack(side="left", expand=True, fill="both")
        for mode in modes:
            mode_selector = Label(selector_frame)
            mode_selector.pack(side="top", expand=True, fill="both")
            mode_label = Label(mode_frame, text=mode, width=8,
                               height=2, font=("Arial", 14))
            if mode == mode_selected:
                mode_selector.config(image=self.__selector_image)
            self.__mode_selector.setdefault(mode, mode_selector)
            mode_label.pack(side="top", expand=True, fill="both")

    def update(self, mode_selected):
        for mode in self.__mode_selector:
            if mode == mode_selected:
                self.__mode_selector[mode].config(image=self.__selector_image)
            else:
                self.__mode_selector[mode].config(image="")
        super().update()


class GameView(Tk, Observer):
    __images: dict[str, PhotoImage] = {}

    def __init__(self, fullscreen=True):
        Tk.__init__(self)
        Observer.__init__(self)
        self.__map_view = None
        self.__menu_frame = None
        self.__pause_frame = None
        self.__fullscreen = fullscreen
        self.resizable(False, False)

        self.attributes("-fullscreen", self.__fullscreen)

    @property
    def map(self):
        return self.__map_view

    @property
    def fullscreen(self):
        return self.__fullscreen

    @fullscreen.setter
    def fullscreen(self, fullscreen):
        self.__fullscreen = fullscreen
        self.attributes("-fullscreen", self.__fullscreen)

    def set_menu_frame(self, modes, mode_selected):
        self.__menu_frame = MenuFrame(self, modes, mode_selected)
        return self.__menu_frame

    def remove_menu_frame(self):
        if self.__menu_frame:
            self.__menu_frame.destroy()

    def set_pause_frame(self):
        self.__pause_frame = PauseFrame(self)
        return self.__pause_frame

    def remove_pause_frame(self):
        if self.__pause_frame:
            self.__pause_frame.destroy()

    def set_map_canvas(self, width, height, background_color):
        self.__map_view = MapView(
            self, width=width, height=height, bg=background_color)
        return self.__map_view

    def remove_map_canvas(self):
        if self.__map_view:
            self.__map_view.destroy()

    def get_image(self, image_path):
        if image_path in self.__images:
            return self.__images[image_path]

    def create_image(self, image_path, width, height):
        image = PhotoImage(file='images/' + image_path + '.png')
        image = image.subsample(4//width, 4//height)
        return self.__images.setdefault(image_path, image)

    def update(self, state=None):
        if state is GameState.PAUSED:
            self.set_pause_frame()
        elif state is GameState.PLAYING and self.__pause_frame:
            self.remove_pause_frame()
        elif state is GameState.PLAYERS_READY:
            self.remove_menu_frame()

        super().update()
