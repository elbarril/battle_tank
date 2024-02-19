class NoPlayersToPlayLevelException(Exception):
    def __init__(self, *args):
        super().__init__("There is no player no play level.", *args)

class MaxPlayersExceededException(Exception):
    def __init__(self, *args):
        super().__init__("The maximum number of players is exceeded.", *args)

class LevelDoesNotExistsException(Exception):
    def __init__(self, *args):
        super().__init__("Level does not exists.", *args)