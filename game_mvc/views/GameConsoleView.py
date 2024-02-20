import keyboard
from models.game.level.Map import Map

class GameConsoleView:
    def show_map(self, map:Map):
        print("")
        for row in map:
            print([obj.symbol for obj in row])

    def listen_keyboard(self, events):
        for key, event in events:
            keyboard.add_hotkey(key, event)

    def loop(self):
        keyboard.wait("esc")