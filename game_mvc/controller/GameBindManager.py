from views import GameView
from typing import Callable


class GameBind:
    def __init__(self, key: str, id: str) -> None:
        self.__key = key
        self.__id = id

    @property
    def key(self) -> str:
        return self.__key

    @property
    def id(self) -> str:
        return self.__id

    def __eq__(self, other):
        if isinstance(other, GameBind):
            return self.key == other.key and self.id == other.id


class GameBindManager:
    def __init__(self, view: GameView) -> None:
        self.__view = view
        self.__binds: list[GameBind] = []

    def add(self, key: str, callable: Callable) -> None:
        id = self.__view.bind(key, callable)
        self.__binds.append(GameBind(key, id))

    def remove(self, bind: GameBind) -> None:
        self.__view.unbind(bind.key, bind.id)
        self.__binds.remove(bind)

    def clear(self) -> None:
        for bind in self:
            self.remove(bind)

    def __iter__(self) -> list[GameBind]:
        return iter(self.__binds)
