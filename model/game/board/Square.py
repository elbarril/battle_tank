from model.game.entity.movable.Tank import Tank
from model.game.entity.movable.Bullet import Bullet
from model.game.entity.Static import Static
from model.game.board.Position import Position

class Square:
    __element:Static = None
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
    def element(self) -> Static:
        return self.__element

    @element.setter
    def element(self, element:Static) -> None:
        self.__element:Static = element

    def add(self, entity):
        if isinstance(entity, Tank):
            self.tank = entity
        elif isinstance(entity, Bullet):
            self.bullet = entity
        elif isinstance(entity, Static):
            self.element = entity

    def get(self, entity):
        if isinstance(entity, Tank):
            return self.tank
        elif isinstance(entity, Bullet):
            return self.bullet
        elif isinstance(entity, Static):
            return self.element

    def remove(self, entity):
        if isinstance(entity, Tank):
            self.tank = None
        elif isinstance(entity, Bullet):
            self.bullet = None
        elif isinstance(entity, Static):
            self.element = None

    def __repr__(self):
        return f"Square(tank={repr(self.tank)}, bullet={repr(self.bullet)}, element={repr(self.element)})"