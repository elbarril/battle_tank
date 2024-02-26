from models.map.MovableObjectDirection import MovableObjectDirections

class PlayerMovements:
    __movements:dict[int, tuple[tuple[str,MovableObjectDirections]]] = {
        1: (
            ("up", MovableObjectDirections.UP),
            ("down", MovableObjectDirections.DOWN),
            ("left", MovableObjectDirections.LEFT),
            ("right", MovableObjectDirections.RIGHT),
        ),
        2: (
            ("w", MovableObjectDirections.UP),
            ("s", MovableObjectDirections.DOWN),
            ("a", MovableObjectDirections.LEFT),
            ("d", MovableObjectDirections.RIGHT),
        )
    }

    @classmethod
    def get(self, player_number:int):
        return self.__movements[player_number]