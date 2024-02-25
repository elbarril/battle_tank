import keyboard
from string import digits
from models.game.level.Map import Map

class GameConsoleView:
    def show_map(self, map:Map):
        print("")
        for row in map:
            print([obj.symbol for obj in row])

    def listen_keyboard(self, key, event):
        keyboard.add_hotkey(key, event)

    def loop(self):
        keyboard.wait("esc")