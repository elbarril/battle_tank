class PlayerAlreadyHasTankException(Exception):
    def __init__(self, *args):
        super().__init__("Player already has a tank.",  *args)

class NotPlayerInstanceException(Exception):
    def __init__(self, *args):
        super().__init__("Not player instance.", *args)

class MissingFirstPlayerException(Exception):
    def __init__(self, *args):
        super().__init__("First Player is missing.", *args)

class MissingSecondPlayerException(Exception):
    def __init__(self, *args):
        super().__init__("Second Player is missing.", *args)