from constants.text import TO_STRING_BOT

class Bot:
    def __init__(self):
        self.tanks = []

    def add_tank(self, tank):
        self.tanks.append(tank)

    def __str__(self):
        return TO_STRING_BOT % self.number