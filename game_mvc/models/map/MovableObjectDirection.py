from models.map.MapObjectPosition import MapObjectPosition

class MovableObjectDirection(MapObjectPosition):
    pass

class MovableObjectDirections:
    UP = MovableObjectDirection(0,-1)
    DOWN = MovableObjectDirection(0,1)
    LEFT = MovableObjectDirection(-1,0)
    RIGHT = MovableObjectDirection(1,0)