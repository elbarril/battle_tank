from typing import Literal

GAME_TITLE:str = "Battle Tank"

POSITIONS_ROWS:int = 10
POSITIONS_COLUMNS:int = 10

FIRST_LEVEL:str = "1"

PLAYER_SPAWN_COLUMN:int = 4
PLAYER_SPAWN_ROW:int = 8
PLAYER_SPAWN_SPEED:int = 1
PLAYER_SPAWN_DIRECTION:Literal["up", "down", "left", "right"] = "down"

UNSET_POSITION = (-1, -1)

LEVELS:dict[str,dict[str,str]] = {
    "1": {
        "elements": [
            ["B","P","P","P","P","P","P","M","P","P"],
            ["P","B","B","B","B","B","P","B","B","P"],
            ["P","B","B","W","W","P","W","W","B","P"],
            ["W","P","P","P","P","P","W","W","P","P"],
            ["W","M","P","F","F","P","P","P","B","P"],
            ["W","S","P","F","F","S","P","P","B","P"],
            ["W","S","E","P","P","P","P","P","B","P"],
            ["P","B","E","P","P","P","P","P","B","P"],
            ["P","S","B","B","P","B","B","B","B","P"],
            ["P","P","P","P","P","P","P","P","P","P"]
        ],
        "bots": []
    },
    "2": {
        "elements": [
            ["P","P","P","P","P","P","P","M","P","P"],
            ["P","B","B","B","B","B","P","B","B","P"],
            ["P","B","B","W","W","P","W","W","B","P"],
            ["W","P","P","B","B","P","W","W","P","P"],
            ["W","M","P","F","F","P","P","P","B","P"],
            ["W","S","P","F","F","S","P","P","B","P"],
            ["W","S","E","P","P","P","P","P","B","P"],
            ["P","B","E","P","P","P","P","P","B","P"],
            ["P","S","B","B","P","B","B","B","B","P"],
            ["P","P","P","P","P","P","P","P","P","P"]
        ],
        "bots": []
    }
}

DISPLAY_WIDTH = 200
DISPLAY_HEIGHT = 100

EXCEPTIONS_MESSAGES = {
    1: "Board postion doesn't exists in column {column}, row {row}",
    2: "Level {level} was not been created in LEVELS.",
    3: "You must call the first level before call the next.",
    4: "{variable} is not a numeric value."
}

EXCODE_POOR = 1
EXCODE_LWNC = 2
EXCODE_FLWNC = 3
EXCODE_VINN = 4

TEST_OUT_OF_LIMITS_COLUMN = 50
TEST_OUT_OF_LIMITS_ROW = 50
TEST_VALID_COLUMN = 2
TEST_VALID_ROW = 2