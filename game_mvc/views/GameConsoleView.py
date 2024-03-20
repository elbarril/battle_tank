import keyboard
from models.map.Map import Map
from views.ViewInterfaz import ViewInterfaz

class GameConsoleView(ViewInterfaz):
    __view_map=[]
    __KEYBOARD = {
        "space": "space",
        "esc": "esc",
        "m": "m",
        "up": "up",
        "down": "down",
        "right": "right",
        "left": "left",
        "w": "w",
        "a": "a",
        "s": "s",
        "d": "d"
    }

    def __init__(self):
        ViewInterfaz.__init__(self, self.__KEYBOARD)

    def show(self, *args):
        print(" ".join((str(arg) for arg in args)))

    def show_map(self, map:Map):
        print("")
        self.__view_map = [[obj.symbol for obj in row if obj] for row in map]
        for row in self.__view_map:
            print(row)

    def update_object_view(self, object):
        pass

    def move_object_view(self, object):
        pass

    def listen_keyboard(self, key, event):
        keyboard.add_hotkey(key, event)

    def shut_keyboard(self, key):
        keyboard.remove_hotkey(key)

    def loop(self, exit_key):
        keyboard.wait(exit_key)