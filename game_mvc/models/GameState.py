from enum import Enum

class GameState(Enum):
    STARTED = 0
    PLAYERS_READY = 1
    LEVEL_READY = 2
    PLAYING = 3
    PAUSED = 4
    GAME_OVER = 5