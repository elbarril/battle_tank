class PlayerEvent:
    from pygame.event import Event
    
    def __init__(self, event:Event):
        from pygame import QUIT as EVENT_QUIT_TYPE, KEYDOWN as EVENT_KEY_DOWN_TYPE
        
        self.__is_key_pressed:bool =  event.type == EVENT_KEY_DOWN_TYPE
        self.__is_quit:bool =  event.type == EVENT_QUIT_TYPE
        self.__key:int|None = event.key if self.__is_key_pressed else None

    @property
    def is_key_pressed(self) -> bool:
        return self.__is_key_pressed
    
    @property
    def is_quit(self) -> bool:
        return self.__is_quit
    
    @property
    def key(self) -> int|None:
        return self.__key