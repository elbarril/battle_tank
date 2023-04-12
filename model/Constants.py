GAME_TITLE:str = "Battle Tank"

SQUARES_ROWS:int = 10
SQUARES_COLUMNS:int = 10

FIRST_LEVEL:int = 1

PLAYER_INITIAL_LIFE:int = 3
PLAYER_SPAWN_COLUMN:int = 4
PLAYER_SPAWN_ROW:int = 8
PLAYER_SPAWN_SPEED:int = 1
PLAYER_SPAWN_DIRECTION:str = "down"

DIRECTION_UP:str = "up"
DIRECTION_DOWN:str = "down"
DIRECTION_LEFT:str = "left"
DIRECTION_RIGHT:str = "right"

UNSET_POSITION:tuple[int,int] = (-1, -1)

LEVELS:list[dict[str,list[list[str]|list[dict[str,int|str]]]]] = [
    {
        "statics": [
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
        "bots": [
            {"column":9,"row":1,"direction":"rigth","speed":1}
        ]
    },
    {
        "statics": [
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
]

DISPLAY_WIDTH:int = 200
DISPLAY_HEIGHT:int = 100

EXCEPTIONS_MESSAGES:dict[int, str] = {
    1: "Board postion doesn't exists in column {column}, row {row}",
    2: "Level {level} was not been created in LEVELS.",
    4: "{variable} is not a numeric value."
}

EXCODE_POOR:int = 1
EXCODE_LWNC:int = 2
EXCODE_VINN:int = 4

TEST_OUT_OF_LIMITS_COLUMN:int = 50
TEST_OUT_OF_LIMITS_ROW:int = 50
TEST_VALID_COLUMN:int = 2
TEST_VALID_ROW:int = 2