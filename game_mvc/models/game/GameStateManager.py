from enum import Enum

class GameState(Enum):
    STARTED = 0
    LEVEL_READY = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4

class GameStateManager:
    def __init__(self):
        self.__game_state = GameState.STARTED

    @property
    def state(self):
        return self.__game_state
    
    def __is_valid_state_transition(self, new_state):
        return new_state in GameState

    def set_game_state(self, new_state):
        if not self.__is_valid_state_transition(new_state):
            self.__game_state = new_state

    def game_init(self):
        self.set_game_state(GameState.STARTED)

    def level_ready(self):
        self.set_game_state(GameState.LEVEL_READY)

    def level_start(self):
        self.set_game_state(GameState.PLAYING)

    def game_over(self):
        self.set_game_state(GameState.GAME_OVER)

    @property
    def is_game_init(self):
        return self.__game_state is GameState.STARTED
    
    @property
    def is_level_ready(self):
        return self.__game_state is GameState.LEVEL_READY
    
    @property
    def is_level_playing(self):
        return self.__game_state is GameState.PLAYING