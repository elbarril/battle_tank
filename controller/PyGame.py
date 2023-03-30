from pygame.time import Clock

class PyGame:
    def __init__(self):
        from pygame import init as py_game_init
        py_game_init()
        self.__clock:Clock = Clock()

    def quit(self) -> None:
        from pygame import quit as py_game_quit
        from sys import exit
        py_game_quit()
        exit()

    @property
    def clock(self) -> Clock:
        return self.__clock

    @property
    def time(self) -> int:
        from pygame import time
        return int(time.get_ticks() / 1000)