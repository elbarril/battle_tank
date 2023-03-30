from model.game.entity.movable.Tank import Tank

class Bot:
    def __init__(self, tank:Tank):
        self.__tank = tank
        
    @property
    def tank(self) -> Tank:
        return self.__tank