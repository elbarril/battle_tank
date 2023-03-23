from pygame import init as py_game_init, quit as py_game_quit
from pygame import QUIT as event_type_quit, KEYDOWN as event_type_key_pressed
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE
from pygame.event import get as py_game_get_events, Event
from typing import List, Union

class PyGame:
    def __init__(self):
        py_game_init()
    
    def get_key_pressed(self, event:Event) -> Union[int, str]:
        return event.key

    @property
    def events(self) -> List[Event]:
        return py_game_get_events()
    
    @property
    def event_type_quit(self) -> int:
        return event_type_quit
    
    @property
    def event_type_key_pressed(self) -> int:
        return event_type_key_pressed
    
    @property
    def moving_keys(self) -> list[int]:
        return [K_UP, K_DOWN, K_LEFT, K_RIGHT]
    
    @property
    def key_up(self) -> int:
        return K_UP
    
    @property
    def key_down(self) -> int:
        return K_DOWN
    
    @property
    def key_left(self) -> int:
        return K_LEFT
    
    @property
    def key_right(self) -> int:
        return K_RIGHT
    
    @property
    def key_space(self) -> int:
        return K_SPACE
    
    def quit(self) -> None:
        py_game_quit()