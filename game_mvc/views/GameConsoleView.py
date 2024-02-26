import keyboard
from models.map.Map import Map

class GameConsoleView:
    def show(self, *args):
        print(*args)

    def show_map(self, map:Map):
        print("")
        for row in map:
            print([obj.symbol for obj in row])

    def listen_keyboard(self, key, event):
        keyboard.add_hotkey(key, event)

    def shut_keyboard(self, key):
        keyboard.remove_hotkey(key)

    def loop(self):
        keyboard.wait("esc")