from model.game.entity.movable.Tank import Tank
from model.game.PlayerEvent import PlayerEvent
from model.game.board.Position import Position
from pygame.event import get as get_player_events

class Player():
    def __init__(self) -> None:
        from model.Constants import (
            PLAYER_SPAWN_COLUMN,
            PLAYER_SPAWN_ROW,
            PLAYER_SPAWN_DIRECTION,
            PLAYER_SPAWN_SPEED,
            PLAYER_INITIAL_LIFE
        )
        self.__tank:Tank = Tank(
                            position=Position(row=PLAYER_SPAWN_ROW, column=PLAYER_SPAWN_COLUMN),
                            direction=PLAYER_SPAWN_DIRECTION,
                            speed=PLAYER_SPAWN_SPEED
                        )
        self.__lifes = PLAYER_INITIAL_LIFE

    @property
    def events(Self) -> list[PlayerEvent]:
        events = []
        for event in get_player_events():
            events.append(PlayerEvent(event))
        return events

    @property
    def tank(self) -> Tank:
        return self.__tank
    
    @property
    def has_lifes(self) -> bool:
        return True if self.__lifes else False
    
    @property
    def lifes(self) -> int:
        return self.__lifes
    
    @lifes.setter
    def lifes(self, lifes:int) -> int:
        self.__lifes = lifes