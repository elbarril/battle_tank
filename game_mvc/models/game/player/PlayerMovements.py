from models.game.level.map.MovableMapObjectDirection import MovableMapObjectDirections

class PlayerMovements:
    __movements = {
        1: (
            ("up", MovableMapObjectDirections.UP),
            ("down", MovableMapObjectDirections.DOWN),
            ("left", MovableMapObjectDirections.LEFT),
            ("right", MovableMapObjectDirections.RIGHT),
        ),
        2: (
            ("w", MovableMapObjectDirections.UP),
            ("s", MovableMapObjectDirections.DOWN),
            ("a", MovableMapObjectDirections.LEFT),
            ("d", MovableMapObjectDirections.RIGHT),
        )
    }

    @classmethod
    def get(self, player_number):
        return self.__movements[player_number]