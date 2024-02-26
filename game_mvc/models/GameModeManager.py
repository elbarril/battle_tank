from models.GameMode import GameMode

class GameModeManager:
    def __init__(self):
        self.__game_mode = GameMode.ONE_PLAYER

    @property
    def mode_value(self):
        return self.__game_mode.value
    
    def __is_valid_mode_transition(self, new_mode):
        return new_mode in GameMode

    def set_game_mode(self, new_mode):
        if self.__is_valid_mode_transition(new_mode):
            self.__game_mode = new_mode

    def one_player(self):
        self.set_game_mode(GameMode.ONE_PLAYER)

    def two_players(self):
        self.set_game_mode(GameMode.TWO_PLAYERS)

    @property
    def is_one_player_mode(self):
        return self.__game_mode is GameMode.ONE_PLAYER

    @property
    def is_two_player_mode(self):
        return self.__game_mode is GameMode.TWO_PLAYERS