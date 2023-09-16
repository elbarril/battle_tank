import tkinter as tk

CANVAS_OFFSET_X = CANVAS_OFFSET_Y = 2

PIXEL_UNIT = MAP_OBJECT_WIDTH_UNIT = MAP_OBJECT_HEIGHT_UNIT = 1
SIZE_PIXELS = 10

WIDTH_PIXELS = HEIGHT_PIXELS = PIXEL_UNIT * SIZE_PIXELS

ROW_SIZE = COLUMN_SIZE = 3

ROW_HEIGHT = ROW_SIZE * HEIGHT_PIXELS
COLUMN_WIDTH = COLUMN_SIZE * WIDTH_PIXELS

MAP_ROWS = MAP_COLUMNS = 15

MAP_HEIGHT = MAP_ROWS * ROW_HEIGHT
MAP_WIDTH = MAP_COLUMNS * COLUMN_WIDTH

WALL_WIDTH = TANK_WIDTH = COLUMN_SIZE
WALL_HEIGHT = TANK_HEIGHT = ROW_SIZE

MAP_COLOR = 'red'

IMAGE_FILE_EXTENSION = '.png'


WALL_MAP_CODE = 1
TANK_MAP_CODE = 2

W = WALL_MAP_CODE
T = TANK_MAP_CODE

MAP = [
    [W,0,0,0,0,0,0,0,0,0,0,0,0,0,W],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,W,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,W,W],
    [W,0,0,0,0,0,0,0,0,0,0,0,0,W,T]
]

class Image(tk.PhotoImage):
    def __init__(self, filename:str, *args, **kwargs):
        super().__init__(file=filename+IMAGE_FILE_EXTENSION, *args, **kwargs)

class Map(tk.Canvas):
    def __init__(self, master:tk.Tk, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.pack()

    def create_image(self, x:int, y:int, image:Image) -> int:
        return super().create_image(x, y, image=image)

class Square:
    def __init__(self, row:int, column:int, width:int, height:int):
        self.__row = row
        self.__column = column
        self.__width = width
        self.__height = height
    
    @property
    def row(self) -> int:
        return self.__row
    
    @property
    def column(self) -> int:
        return self.__column

    @property
    def _width_radio(self) -> int:
        return self.__width / 2

    @property
    def _width(self) -> int:
        return self.__width

    @property
    def _height_radio(self) -> int:
        return self.__height / 2

    @property
    def _height(self) -> int:
        return self.__height
    
    @property
    def left(self) -> int:
        return self.column - self._width_radio

    @property
    def top(self) -> int:
        return self.row - self._height_radio

    @property
    def right(self) -> int:
        return self.column + self._width_radio

    @property
    def bottom(self) -> int:
        return self.row + self._height_radio

from abc import ABC, abstractmethod

class MapObject(Square, ABC):
    def __init__(self, map:Map, image:Image, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__map = map
        self.__image = image

    @property
    def map(self) -> Map:
        return self.__map

    @property
    def image(self) -> Image:
        return self.__image

    @property
    def x(self) -> int:
        return (self.column * self._width + self._width_radio) * WIDTH_PIXELS + CANVAS_OFFSET_X

    @property
    def y(self) -> int:
        return (self.row * self._height + self._height_radio) * HEIGHT_PIXELS + CANVAS_OFFSET_Y

    @abstractmethod
    def create(self):
        self.__id = self.__map.create_image(self.x, self.y, self.image)


class SingleMapObject(MapObject):
    def __init__(self, map:Map, image:Image, *args, **kwargs):
        super().__init__(map, image, *args, **kwargs)

    def create(self):
        super().create()

class MultipleMapObject(MapObject):
    def __init__(self, map:Map, image:Image, *args, **kwargs):
        super().__init__(map, image, *args, **kwargs)
        self.__map_objects:list[SingleMapObject] = []
    
    def create(self):
        for y in range(self._height):
            row = self.row * self._height + y
            for x in range(self._width):
                column = self.column * self._width + x
                map_object = SingleMapObject(self.map, self.image, row, column, MAP_OBJECT_WIDTH_UNIT, MAP_OBJECT_HEIGHT_UNIT)
                map_object.create()
                self.__map_objects.append(map_object)

    @property
    def map_objects(self) -> list[SingleMapObject]:
        return self.__map_objects

class Wall(MultipleMapObject):
    def __init__(self, map:Map, row:int, column:int):
        super().__init__(map, self.image, row, column, WALL_WIDTH, WALL_HEIGHT)

class Tank(SingleMapObject):
    def __init__(self, map:Map, row:int, column:int):
        super().__init__(map, self.image, row, column, TANK_WIDTH, TANK_HEIGHT)

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__map = Map(self, width=MAP_WIDTH, height=MAP_HEIGHT, bg=MAP_COLOR)
        self.__map.pack()

        Tank.image = Image("playertank_up")
        Wall.image = Image("brick")

    def load(self):
        for row in range(len(MAP)):
            for column in range(len(MAP[row])):
                MAP_CODE = MAP[row][column]
                if not MAP_CODE: continue
                elif MAP_CODE == TANK_MAP_CODE: Tank(self.__map, row, column).create()
                elif MAP_CODE == WALL_MAP_CODE: Wall(self.__map, row, column).create()

        self.mainloop()

Game().load()