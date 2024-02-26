import keyboard
from models.game.Map import Map

class GameConsoleView:
    def show(self, *args):
        print(*args)

    def show_map(self, map:Map):
        print("")
        for row in map:
            print([obj.symbol for obj in row])

    def listen_keyboard(self, key, event):
        keyboard.add_hotkey(key, event)

    def loop(self):
        keyboard.wait("esc")