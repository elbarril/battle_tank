from models.game.level.map.MapObjectPosition import MapObjectPosition

class MapObjectDirection(MapObjectPosition):
    pass

class MovableMapObjectDirections:
    UP = MapObjectDirection(0,-1)
    DOWN = MapObjectDirection(0,1)
    LEFT = MapObjectDirection(-1,0)
    RIGHT = MapObjectDirection(1,0)