import tkinter as tk
from abc import ABC, abstractmethod
from threading import Thread
import time
import random

POSITION = 1
PIXELS = 10

MIN_OBJECT_POSITIONS = 1*POSITION
MAX_OBJECT_POSITIONS = 4*POSITION
POSITION_PIXELS = POSITION*PIXELS

ROW_POSITIONS = COLUMN_POSITIONS = MAX_OBJECT_POSITIONS

ROW_HEIGHT = ROW_POSITIONS * POSITION_PIXELS
COLUMN_WIDTH = COLUMN_POSITIONS * POSITION_PIXELS

MAP_ROWS = 15
MAP_COLUMNS = 15

MAP_HEIGHT = MAP_ROWS * ROW_HEIGHT
MAP_WIDTH = MAP_COLUMNS * COLUMN_WIDTH

WALL_WIDTH = TANK_WIDTH = MAX_OBJECT_POSITIONS * POSITION_PIXELS
WALL_HEIGHT = TANK_HEIGHT = MAX_OBJECT_POSITIONS * POSITION_PIXELS

BRICK_WIDTH = MIN_OBJECT_POSITIONS * 2 * POSITION_PIXELS
BRICK_HEIGHT = MIN_OBJECT_POSITIONS * 2 * POSITION_PIXELS

BULLET_WIDTH = MIN_OBJECT_POSITIONS * POSITION_PIXELS
BULLET_HEIGHT = MIN_OBJECT_POSITIONS * POSITION_PIXELS

MAP_COLOR = 'darkgrey'

IMAGE_FILE_EXTENSION = '.png'

DIR_KEY_UP = "w"
DIR_KEY_LEFT = "a"
DIR_KEY_DOWN = "s"
DIR_KEY_RIGHT = "d"

DIRECTION_KEYS = [
    DIR_KEY_UP,
    DIR_KEY_LEFT,
    DIR_KEY_DOWN,
    DIR_KEY_RIGHT
]

DIR_UP = (-1*PIXELS, 0*PIXELS)
DIR_LEFT = (0*PIXELS, -1*PIXELS)
DIR_DOWN = (1*PIXELS, 0*PIXELS)
DIR_RIGHT = (0*PIXELS, 1*PIXELS)

DIRECTIONS:dict[str, tuple[int,int]] = {
    DIR_KEY_DOWN: DIR_DOWN,
    DIR_KEY_LEFT: DIR_LEFT,
    DIR_KEY_UP: DIR_UP,
    DIR_KEY_RIGHT: DIR_RIGHT
}

BULLET_MAP_CODE = "b"
PLAYER_MAP_CODE = 1
BOT_MAP_CODE = 2
WALL_MAP_CODE = 3

P = PLAYER_MAP_CODE
B = BOT_MAP_CODE
W = WALL_MAP_CODE

MAP_OBJECTS = [P, B, W]

FIRST_LEVEL = 1
LEVELS = 1
LEVEL_MAPS = {
    FIRST_LEVEL: [
        [B,0,0,0,0,0,0,0,0,0,0,0,0,0,W],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,W,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,P,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,W,W],
        [W,0,0,0,0,0,0,0,0,0,0,0,0,W,B]
    ]
}

DIRECTION_IMAGE_SUFFIX = {
    DIR_KEY_UP: "_up",
    DIR_KEY_LEFT: "_left",
    DIR_KEY_DOWN: "_down",
    DIR_KEY_RIGHT: "_right"
}

BULLET_IMAGE_FILENAME = "bullet"
PLAYER_IMAGE_FILENAME = "playertank"
BOT_IMAGE_FILENAME = "bottank"
WALL_IMAGE_FILENAME = "brick"

class Image(tk.PhotoImage):
    def __init__(self, filename:str, *args, **kwargs):
        super().__init__(file=filename+IMAGE_FILE_EXTENSION, *args, **kwargs)

class MapObjectSize:
    def __init__(self, width:int, height:int):
        self.__width = width
        self.__height = height
        
    @property
    def width(self): return self.__width

    @property
    def height(self): return self.__height

class Square:
    def __init__(self, size:MapObjectSize):
        self.__size = size

    @property
    def width_radio(self): return self.__size.width / 2

    @property
    def height_radio(self): return self.__size.height / 2

    @property
    def width(self): return self.__size.width

    @property
    def height(self): return self.__size.height

class MapObjectPosition:
    def __init__(self, x:int, y:int):
        self._x = x
        self._y = y

    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    @x.setter
    def x(self, x:int): self._x = x
    
    @y.setter
    def y(self, y:int): self._y = y

    def __str__(self): return f"x:{self.x}, y:{self.y}"

class MapObject(Square, ABC):
    def __init__(self, position:MapObjectPosition, image:Image, size:MapObjectSize):
        super().__init__(size)
        self.__id:int = None
        self.__code:int = None
        self.__position = position
        self.__image = image

    @property
    def position(self): return self.__position

    @position.setter
    def position(self, position:MapObjectPosition): self.__position = position

    @property
    def x0(self): return self.__position.x

    @property
    def x1(self): return self.__position.x + self.width

    @property
    def y0(self): return self.__position.y

    @property
    def y1(self): return self.__position.y + self.height

    @property
    def id(self): return self.__id

    @id.setter
    def id(self, id:int): self.__id = id

    @property
    def code(self): return self.__code

    @code.setter
    def code(self, code:int): self.__code = code

    @property
    def image(self): return self.__image

    @image.setter
    def image(self, image:Image): self.__image = image

    @property
    @abstractmethod
    def list(self): return [self]

class SingleMapObject(MapObject):
    def __init__(self, position:MapObjectPosition, image:Image, size:MapObjectSize):
        super().__init__(position, image, size)

    @property
    def list(self): return super().list

class MultipleMapObject(MapObject):
    def __init__(self, position:MapObjectPosition, image:Image, max_size:MapObjectSize, min_size:MapObjectSize):
        super().__init__(position, image, max_size)
        self.__map_objects:list[SingleMapObject] = []

        rows = self.height // min_size.height
        columns = self.width // min_size.width
        for row in range(rows):
            for column in range(columns):
                position_x = self.position.x + column * min_size.width
                position_y = self.position.y + row * min_size.height
                position = MapObjectPosition(x=position_x, y=position_y)
                map_object = SingleMapObject(position, self.image, min_size)
                self.__map_objects.append(map_object)

    @property
    def list(self): return self.__map_objects

class Wall(MultipleMapObject):
    __wall_size = MapObjectSize(WALL_WIDTH, WALL_HEIGHT)
    __brick_size = MapObjectSize(BRICK_WIDTH, BRICK_HEIGHT)
    def __init__(self, map_positions:MapObjectPosition, image:Image):
        super().__init__(map_positions, image, self.__wall_size, self.__brick_size)
        self.code = WALL_MAP_CODE

class MovableSingleMapObject(SingleMapObject):
    def __init__(self, position:MapObjectPosition, direction:str, images:dict[str,Image], size:MapObjectSize):
        super().__init__(position, images[direction], size)
        self.__direction = direction
        self.__images = images

    @property
    def direction(self): return self.__direction
    
    @direction.setter
    def direction(self, direction:str):
        self.image = self.__images[direction]
        self.__direction = direction
    
    def move(self):
        move_y, move_x = DIRECTIONS[self.direction]
        self.position.x += move_x
        self.position.y += move_y

    @property
    def next_area(self):
        move_y, move_x = DIRECTIONS[self.direction]
        left = self.x0 + move_x
        top = self.y0 + move_y
        right = self.x1 + move_x
        bottom = self.y1 + move_y
        return (left, top, right, bottom)

class Bullet(MovableSingleMapObject):
    __bullet_size = MapObjectSize(BULLET_WIDTH, BULLET_HEIGHT)
    def __init__(self, position:MapObjectPosition, images:dict[str,Image], direction:str):
        super().__init__(position, direction, images, self.__bullet_size)
        self.code = BULLET_MAP_CODE

class Tank(MovableSingleMapObject):
    __tank_size = MapObjectSize(TANK_WIDTH, TANK_HEIGHT)
    def __init__(self, position:MapObjectPosition, images:dict[str,Image]):
        super().__init__(position, DIR_KEY_UP, images["tank"], self.__tank_size)
        self.__bullet_images = images["bullet"]

    def shoot(self) -> Bullet:
        move_y, move_x = DIRECTIONS[self.direction]
        y = self.position.y + move_y*self.height_radio/PIXELS + self.height_radio - BULLET_HEIGHT/2
        x = self.position.x + move_x*self.width_radio/PIXELS + self.width_radio - BULLET_WIDTH/2
        return Bullet(MapObjectPosition(x, y), self.__bullet_images, self.direction)

class Player:
    def __init__(self):
        self.__tank = None

    @property
    def tank_images(self): return self.__tank_images

    @tank_images.setter
    def tank_images(self, tank_images:dict[str,Image]): self.__tank_images = tank_images

    @property
    def tank(self) -> Tank:
        return self.__tank

    @tank.setter
    def tank(self, tank:Tank) -> None:
        tank.code = PLAYER_MAP_CODE
        self.__tank = tank

class Map(tk.Canvas):
    def __init__(self, master:tk.Tk, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.pack()
        self.__map_objects:dict[int,MapObject] = {}

    def create(self, map_object:MapObject) -> MapObject:
        for object in map_object.list:
            map_x = object.position.x + object.width_radio
            map_y = object.position.y + object.height_radio
            object.id = self.create_image(map_x, map_y, image=object.image)
            self.__map_objects.setdefault(object.id, object)
        self.update()
        return map_object
    
    def move(self, map_object:MapObject) -> None:
        self.coords(map_object.id, map_object.position.x, map_object.position.y)
        self.update()

    def remove(self, map_object:MapObject) -> None:
        self.delete(map_object.id)
        self.__map_objects.pop(map_object.id)
        self.update()

    def can_move_in_area(self, area:tuple[int,int,int,int]) -> bool:
        left, top, right, bottom = area
        return  left >= 0 and  top >= 0 and right <= MAP_WIDTH and bottom <= MAP_HEIGHT

    def get_collided_objects_by_area(self, area:tuple[int,int,int,int]):
        left, top, right, bottom = area
        map_object_ids = list(self.find_overlapping(left, top, right, bottom))
        map_objects = [object for id in map_object_ids for object in self.__map_objects.get(id).list]
        map_objects = [self.__map_objects.get(id) for id in map_object_ids]
        return map_objects

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__fullscreen = True
        self.attributes("-fullscreen", self.__fullscreen)

        self.__map = Map(self, width=MAP_WIDTH, height=MAP_HEIGHT, bg=MAP_COLOR)
        self.__map.pack()

        self.__players:list[Player] = []
        self.__bot = Bot(self)

        self.__bullets:list[Bullet] = []
        self.__bullet_mover:Thread = None

    def load(self, level_id:int=FIRST_LEVEL):
        level = Level(level_id)
        for map_object in level.map_objects:
            self.__map.create(map_object)
        
        for player in level.player_tanks:
            player = Player()
            player.tank = tank
            self.__players.append(player)

        for tank in level.bot_tanks:
             self.__bot.add_tank(tank)

        return self

    def start(self):
        for player in self.__players:
            for direction_key in DIRECTION_KEYS: self.bind(direction_key, lambda e,t=player.tank,dk=direction_key:self.move_tank(t,dk))
            self.bind("<space>", lambda e,t=player.tank:self.tank_shoots(t))
        self.bind("<Escape>", lambda e,window=self:self.end(window))
        self.bind("f", lambda e,window=self:self.toggle_fullscreen(window))
        self.__bot.play()
        self.mainloop()

    def toggle_fullscreen(self, window:tk.Tk):
        self.__fullscreen = False if self.__fullscreen else True
        window.attributes("-fullscreen", self.__fullscreen)

    def end(self, window:tk.Tk):
        self.__unbind_player_events()
        if self.__fullscreen: window.attributes("-fullscreen", False)
        window.quit()

    def move_tank(self, tank:Tank, direction:str):
        if tank.direction != direction:
            tank.direction = direction
            self.__map.remove(tank)
            tank = self.__map.create(tank)

        elif self.__map.can_move_in_area(tank.next_area):
            collided_objects = self.__get_collided_objects_in_next_area(tank)
            if len(collided_objects): return
            self.__map.move(tank)
            tank.move()

    def tank_shoots(self, tank:Tank) -> None:
        bullet = tank.shoot()
        self.__bullets.append(bullet)
        self.__map.create(bullet)
        if not self.__bullet_mover or not self.__bullet_mover.is_alive():
            self.__bullet_mover = Thread(target=self.__move_bullets)
            self.__bullet_mover.daemon = True
            self.__bullet_mover.start()
    
    def __move_bullets(self):
        while len(self.__bullets):
            for bullet in self.__bullets:
                self.__move_bullet(bullet)
            time.sleep(.05)
    
    def __move_bullet(self, bullet:Bullet):
        if self.__map.can_move_in_area(bullet.next_area):
            collided_objects = self.__get_collided_objects_in_next_area(bullet)
            if len(collided_objects):
                self.__remove_map_object(bullet)
                self.__remove_map_object(collided_objects[0])
            else:
                self.__map.move(bullet)
                bullet.move()
        else: self.__remove_map_object(bullet)

    def __remove_map_object(self, map_object):
        self.__map.remove(map_object)
        if isinstance(map_object, Tank):
            player_tanks = [player.tank for player in self.__players]
            if map_object in player_tanks:
                self.__players.remove(player_tanks.index(map_object))
                if not len(self.__players): self.end(self)
            else: self.__bot.remove_tank(map_object)
        elif isinstance(map_object, Bullet):
            self.__bullets.remove(map_object)

    def __unbind_player_events(self, player:Player):
        for direction_key in DIRECTION_KEYS: self.unbind(direction_key)
        self.unbind("<space>")

    def __get_collided_objects_in_next_area(self, movable_map_object:MovableSingleMapObject):
        map_objects = self.__map.get_collided_objects_by_area(movable_map_object.next_area)
        if movable_map_object in map_objects: map_objects.remove(movable_map_object)
        return map_objects

class Bot(Player):
    def __init__(self, game:Game):
        super().__init__()
        self.__tanks:list[Tank] = []
        self.__game = game

    def add_tank(self, tank:Tank):
        tank.code = BOT_MAP_CODE
        self.__tanks.append(tank)

    def remove_tank(self, tank:Tank):
        self.__tanks.remove(tank)

    def play(self):
        self.__bot = Thread(target=self.__bot_ia)
        self.__bot.daemon = True
        self.__bot.start()

    def __bot_ia(self):
        while len(self.__tanks):
            for tank in self.__tanks:
                time.sleep(.5)
                move = lambda t=tank,dk=random.choice(DIRECTION_KEYS): self.__game.move_tank(t,dk)
                shoots = lambda t=tank: self.__game.tank_shoots(t)
                action = random.choice([move, shoots])
                action()

class Level:
    __map_objects_classes = {
        PLAYER_MAP_CODE: Tank,
        BOT_MAP_CODE: Tank,
        WALL_MAP_CODE: Wall
    }

    def __init__(self, id:int):
        MAP = LEVEL_MAPS[id]
        self.__map_objects:dict[int,MapObject] = {MAP_CODE:[] for MAP_CODE in MAP_OBJECTS}

        self.__map_objects_images = {
            PLAYER_MAP_CODE: {DIR_KEY: Image(PLAYER_IMAGE_FILENAMES[DIR_KEY]) for DIR_KEY in DIRECTION_KEYS},
            BOT_MAP_CODE: {DIR_KEY: Image(BOT_IMAGE_FILENAMES[DIR_KEY]) for DIR_KEY in DIRECTION_KEYS},
            WALL_MAP_CODE: Image(WALL_IMAGE_FILENAME)
        }

        for row in range(len(MAP)):
            for column in range(len(MAP[row])):
                map_object:MapObject = None
                map_code = MAP[row][column]
                if map_code:
                    position = MapObjectPosition(x=column*COLUMN_WIDTH, y=row*ROW_HEIGHT)
                    map_object = self.__create_map_object(map_code, position, self.__map_objects_images[map_code])
                    self.__map_objects[map_code].append(map_object)

    @property
    def map_objects(self): return list(self.__map_objects.values())

    @property
    def player_tanks(self): return self.__map_objects[PLAYER_MAP_CODE]

    @property
    def bot_tanks(self): return self.__map_objects[BOT_MAP_CODE]

    @classmethod
    def __create_map_object(cls, map_code:int, *args, **kwargs):
        return cls.__map_objects_classes[map_code](*args, **kwargs) 
  
Game().load().start()