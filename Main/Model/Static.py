from Main.Model.MapElement import MapElement

class Static(MapElement):
    def __init__(self, column:int, row:int, is_solid:bool):
        self.__column:int = column
        self.__row:int = row
        self.__is_solid:bool = is_solid
    
    @property
    def column(self) -> int:
        return self.__column
    
    @column.setter
    def column(self, column:int) -> None:
        self.__column:int = column

    @property
    def row(self) -> int:
        return self.__row
    
    @row.setter
    def row(self, row) -> int:
        self.__row:int = row
    
    @property
    def is_solid(self) -> bool:
        return self.__is_solid
    
    @is_solid.setter
    def is_solid(self, is_solid:bool) -> bool:
        self.__is_solid:bool = is_solid        
        
    