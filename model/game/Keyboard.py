from pygame import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE
)

class Keyboard:
    @classmethod    
    def is_direction_key(self, key:int) -> bool:
        return key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]
    
    @classmethod    
    def is_shoot_key(self, key:int) -> bool:
        return key in [K_SPACE]