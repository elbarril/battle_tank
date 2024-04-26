from enum import Enum

class GameState(Enum):
    STARTED = 0
    PLAYERS_READY = 1
    LEVEL_READY = 2
    PLAYING = 3
    PAUSED = 4
    GAME_OVER = 5

class GameStateManager:
    def __init__(self):
        self.__game_state:GameState = None
        self.__valid_transitions = {
            None: [GameState.STARTED],
            GameState.STARTED: [GameState.PLAYERS_READY],
            GameState.PLAYERS_READY: [GameState.LEVEL_READY],
            GameState.LEVEL_READY: [GameState.PLAYING],
            GameState.PLAYING: [GameState.PAUSED, GameState.GAME_OVER],
            GameState.PAUSED: [GameState.PLAYING, GameState.STARTED]
        }

    @property
    def state(self):
        return self.__game_state
    
    def __is_valid_state_transition(self, new_state):
        return new_state in self.__valid_transitions[self.__game_state]

    def set_game_state(self, new_state:GameState):
        if self.__is_valid_state_transition(new_state):
            self.__game_state = new_state
            print(self.__game_state.name)
        else:
            raise RuntimeError(f"Wrong next state: {new_state}. Current state: {self.__game_state}")

    def game_init(self):
        self.set_game_state(GameState.STARTED)

    def players_ready(self):
        self.set_game_state(GameState.PLAYERS_READY)

    def level_ready(self):
        self.set_game_state(GameState.LEVEL_READY)

    def level_start(self):
        self.set_game_state(GameState.PLAYING)

    def level_paused(self):
        self.set_game_state(GameState.PAUSED)

    def game_over(self):
        self.set_game_state(GameState.GAME_OVER)

    @property
    def is_game_init(self):
        return self.__game_state is GameState.STARTED
    
    @property
    def is_players_ready(self):
        return self.__game_state is GameState.PLAYERS_READY
    
    @property
    def is_level_ready(self):
        return self.__game_state is GameState.LEVEL_READY
    
    @property
    def is_level_playing(self):
        return self.__game_state is GameState.PLAYING
    
    @property
    def is_level_paused(self):
        return self.__game_state is GameState.PAUSED
    
    @property
    def is_level_game_over(self):
        return self.__game_state is GameState.GAME_OVER