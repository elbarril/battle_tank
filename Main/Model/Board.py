from Main.Model.Square import Square
from Main.Model.Static import Static
from Main.Model.Movable import Movable
from Main.Model.Tank import Tank
from Main.Model.Bullet import Bullet
from Main.Model.Constants import (
    POSITIONS_COLUMNS,
    POSITIONS_ROWS,
    EXCEPTIONS_MESSAGES,
    EXCODE_POOR
)
class Board:
    __instance = None
    __positions:list[list[Square]] = []
    __bullets:list[Bullet] = []

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.initialize()
        return cls.__instance

    @classmethod
    def initialize(cls):
        cls.__instance = cls()
        cls.__positions = [[Square() for _ in range(POSITIONS_ROWS)] for _ in range(POSITIONS_COLUMNS)]

    def __is_valid_position(self, row:int, column:int) -> bool:
        return not ((column < 0 or row < 0) or (row >= len(self.positions) or column >= len(self.positions[row])))

    @property
    def positions(self) -> list[list[Square]]:
        return self.__positions
    
    @property
    def bullets(self) -> list[Bullet]:
        return self.__bullets

    def add_level_elements(self, level_elements:list[Static]) -> None:
        for level_element in level_elements:
            self.add_element(level_element)
    
    def detect_collision(self, moving_element:Movable) -> bool:
        if self.__is_valid_position(moving_element.next_row, moving_element.next_column):
            element:Static = self.positions[moving_element.next_row][moving_element.next_column].element
            tank:Tank = self.positions[moving_element.next_row][moving_element.next_column].tank
            bullet:Bullet = self.positions[moving_element.next_row][moving_element.next_column].bullet
            return element.is_solid or tank or bullet
        return True
    
    def add_element(self, element:Static) -> None:
        if self.__is_valid_position(element.row, element.column):
            self.positions[element.row][element.column].element:Static = element
        else:
            raise Exception(EXCEPTIONS_MESSAGES[EXCODE_POOR].format(column=element.column, row=element.row))
        
    def get_position(self, row, column) -> Square:
        if self.__is_valid_position(row, column):
            return self.positions[row][column]
        else:
            raise Exception(EXCEPTIONS_MESSAGES[EXCODE_POOR].format(column=column, row= row))
    
    def remove_element(self, element:Static) -> None:
        if self.__is_valid_position(element.row, element.column):
            del self.positions[element.row][element.column].element
        else:
            raise Exception(EXCEPTIONS_MESSAGES[EXCODE_POOR].format(column=element.column, row=element.row))
    
    def add_tank(self, tank:Tank) -> None:
        if self.__is_valid_position(tank.row, tank.column):
            self.positions[tank.row][tank.column].tank:Tank = tank
        else:
            raise Exception(EXCEPTIONS_MESSAGES[EXCODE_POOR].format(column=tank.column, row=tank.row))
    
    def remove_tank(self, tank:Tank) -> None:
        if self.__is_valid_position(tank.row, tank.column):
            del self.positions[tank.row][tank.column].tank
        else:
            raise Exception(EXCEPTIONS_MESSAGES[EXCODE_POOR].format(column=tank.column, row=tank.row))
    
    def remove_previous_tank(self, tank:Tank) -> None:
        if self.__is_valid_position(tank.previous_row, tank.previous_column):
            del self.positions[tank.previous_row][tank.previous_column].tank

    def add_bullet(self, bullet:Bullet) -> None:
        if self.__is_valid_position(bullet.row, bullet.column):
            self.positions[bullet.row][bullet.column].bullet:Bullet = bullet
        else:
            raise Exception(EXCEPTIONS_MESSAGES[EXCODE_POOR].format(column=bullet.column, row=bullet.row))

    def remove_bullet(self, bullet:Bullet) -> None:
        if self.__is_valid_position(bullet.row, bullet.column):
            del self.positions[bullet.row][bullet.column].bullet
            self.bullets.remove(bullet)
        else:
            raise Exception(EXCEPTIONS_MESSAGES[EXCODE_POOR].format(column=bullet.column, row=bullet.row))

    def remove_previous_bullet(self, bullet:Bullet) -> None:
        if self.__is_valid_position(bullet.previous_row, bullet.previous_column):
            del self.positions[bullet.previous_row][bullet.previous_column].bullet
        else:
            raise Exception(EXCEPTIONS_MESSAGES[EXCODE_POOR].format(column=bullet.previous_column, row=bullet.previous_row))