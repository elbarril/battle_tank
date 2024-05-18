class Observer:
    def update(self): pass


class Observable:
    def __init__(self):
        self._observers: list[Observer] = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(*args, **kwargs)
