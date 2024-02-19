class WrongPositionValueTypeException(Exception):
    def __init__(self, *args):
        super().__init__("Wrong position value type.", *args)

class NotPositionTypeException(Exception):
    def __init__(self, *args):
        super().__init__("Wrong position type.", *args)