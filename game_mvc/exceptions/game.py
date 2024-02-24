class LevelDoesNotExistsException(Exception):
    def __init__(self, *args):
        super().__init__("Level does not exists.", *args)