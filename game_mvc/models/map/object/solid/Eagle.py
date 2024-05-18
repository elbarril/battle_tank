from ..abstract.SolidMapObject import SolidMapObject


class Eagle(SolidMapObject):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.image = 'eagle'

    def __str__(self):
        return "Eagle p:%s s:%s" % (self.position, self.size)
