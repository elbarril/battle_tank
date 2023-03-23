from Main.Model.Tank import Tank

class Bot:
    def __init__(self, tank):
        self.__tank = Tank(tank)
        
    def getTank(self):
        return self.__tank