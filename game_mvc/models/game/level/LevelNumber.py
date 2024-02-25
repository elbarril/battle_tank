from constants.game import MAX_LEVEL_NUMBER

class LevelNumber:
    def __init__(self, number):
        if (isinstance(number, int) and (number > 0 and number <= MAX_LEVEL_NUMBER)):
            self.number = "0" + str(number) if len(str(number)) == 1 else str(number)
        
    def __str__(self):
        return self.number