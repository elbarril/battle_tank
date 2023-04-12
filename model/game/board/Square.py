from model.game.entity.movable.Tank import Tank
from model.game.entity.movable.Bullet import Bullet
from model.game.entity.Static import Static
from model.game.board.Position import Position

class Square:
    __static:Static = None
    __tank:Tank = None
    __bullet:Bullet = None

    @property
    def bullet(self) -> Bullet:
        return self.__bullet

    @bullet.setter
    def bullet(self, bullet:Bullet) -> None:
        self.__bullet:Bullet = bullet
    
    @property
    def tank(self) -> Tank:
        return self.__tank

    @tank.setter
    def tank(self, tank:Tank) -> None:
        self.__tank:Tank = tank

    @property
    def static(self) -> Static:
        return self.__static

    @static.setter
    def static(self, static:Static) -> None:
        self.__static:Static = static

    def add(self, entity):
        if isinstance(entity, Tank):
            self.tank = entity
        elif isinstance(entity, Bullet):
            self.bullet = entity
        elif isinstance(entity, Static):
            self.static = entity

    def get(self, entity):
        if isinstance(entity, Tank):
            return self.tank
        elif isinstance(entity, Bullet):
            return self.bullet
        elif isinstance(entity, Static):
            return self.static

    def remove(self, entity):
        if isinstance(entity, Tank):
            self.tank = None
        elif isinstance(entity, Bullet):
            self.bullet = None
        elif isinstance(entity, Static):
            self.static = None

    def __repr__(self):
        return f"Square(tank={repr(self.tank)}, bullet={repr(self.bullet)}, static={repr(self.static)})"