from models.map.MapPosition import MapPosition

class MovableObjectDirection(MapPosition):
    pass

class MovableObjectDirections:
    UP = MovableObjectDirection(0,-1)
    DOWN = MovableObjectDirection(0,1)
    LEFT = MovableObjectDirection(-1,0)
    RIGHT = MovableObjectDirection(1,0)