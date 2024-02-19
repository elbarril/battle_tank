from constants.level import MAX_LEVEL_NUMBER
from exceptions.level import WrongOrEmptyLevelNumber

class LevelNumber:
    def __init__(self, number):
        if not (isinstance(number, int) and (number > 0 and number <= MAX_LEVEL_NUMBER)):
            raise WrongOrEmptyLevelNumber(f"Number must to be an integer from 1 to {MAX_LEVEL_NUMBER}")
        self.number = "0" + str(number) if len(str(number)) == 1 else str(number)
        
    def __str__(self):
        return self.number