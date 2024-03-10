class PlayerShoot:
    __shoot:dict[int, str] = {
        1: "m",
        2: "space"
    }

    @classmethod
    def get(self, player_number:int):
        return self.__shoot[player_number]