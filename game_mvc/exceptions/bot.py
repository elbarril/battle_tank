class BotPlayerAlreadyHasTankException(Exception):
    def __init__(self, *args):
        super().__init__("Bot player already has a tank.", *args)