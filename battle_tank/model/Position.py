class Position:
    def __init__(self, x:int, y:int):
        self._x = x
        self._y = y

    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    @x.setter
    def x(self, x:int): self._x = x
    
    @y.setter
    def y(self, y:int): self._y = y

    def __str__(self): return f"x:{self.x}, y:{self.y}"