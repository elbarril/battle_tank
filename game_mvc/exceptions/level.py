class WrongOrEmptyLevelNumber(Exception):
    def __init__(self, *args):
        super().__init__("Wrong or empty level number.", *args)

class NonExistentMapLevelNumber(Exception):
    def __init__(self, *args):
        super().__init__("There is not level map data.", *args)

class MapDoesNotExistsException(Exception):
    def __init__(self, *args):
        super().__init__("Level map does not exists.", *args)