from abc import ABC, abstractmethod

class ViewInterfaz(ABC):
    def __init__(self, keyboard):
        self.__keyboard = keyboard

    @abstractmethod
    def show(self, *args):
        pass

    @abstractmethod
    def show_map(self, map):
        pass

    @abstractmethod
    def listen_keyboard(self, key, event):
        pass

    @abstractmethod
    def shut_keyboard(self, key):
        pass

    @abstractmethod
    def loop(self):
        pass

    def _get_key(self, key):
        return self.__keyboard[key]