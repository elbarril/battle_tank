class MapDataHasNotRowsException(Exception):
    def __init__(self, *args):
        super().__init__("Wrong rows in map data.")

class WrongPositionDataException(Exception):
    def __init__(self, *args):
        super().__init__("Wrong position data.", *args)

class WrongSizeDataException(Exception):
    def __init__(self, *args):
        super().__init__("Wrong size data.", *args)

class WrongDirectionDataException(Exception):
    def __init__(self, *args):
        super().__init__("Wrong direction data.", *args)

class NotValidMapObjectException(Exception):
    def __init__(self, *args):
        super().__init__("Not valid map object.", *args)

class WrongMapObjectSymbol(Exception):
    def __init__(self, *args):
        super().__init__("Wrong map object symbol.", *args)

class NonExistentMapLevelNumber(Exception):
    def __init__(self, *args):
        super().__init__("There is not level map data.", *args)
        