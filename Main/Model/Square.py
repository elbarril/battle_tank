from Main.Model.Tank import Tank
from Main.Model.Bullet import Bullet
from Main.Model.Static import Static

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

    @bullet.deleter
    def bullet(self) -> None:
        if self.__bullet:
            del self.__bullet
    
    @property
    def tank(self) -> Tank:
        return self.__tank

    @tank.setter
    def tank(self, tank:Tank) -> None:
        self.__tank:Tank = tank

    @tank.deleter
    def tank(self) -> None:
        if self.__tank:
            del self.__tank

    @property
    def element(self) -> Static:
        return self.__element

    @element.setter
    def element(self, element:Static) -> None:
        self.__element:Static = element

    @element.deleter
    def element(self) -> None:
        if self.__element:
            del self.__element