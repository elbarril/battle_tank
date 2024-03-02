from models.map.MapPosition import MapPosition

class MapObjectPosition:
    def __init__(self, map_positions:list[MapPosition]):
        self.__map_positions = map_positions

    def __len__(self):
        return len(self.__map_positions)
    
    def __getitem__(self, index) -> MapPosition:
        return self.__map_positions[index]

    def __iter__(self):
        return iter(self.__map_positions)
    
    def __add__(self, other):
        if isinstance(other, MapPosition):
            return MapObjectPosition([position + other for position in self.__map_positions])

    def __radd__(self, other):
        return self.__add__(other)
    
    def __str__(self):
        return str([str(p) for p in self.__map_positions])