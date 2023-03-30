class Position:
    def __init__(self, row:int, column:int) -> None:
        self.__row:int = row
        self.__column:int = column

    @property
    def row(self) -> int:
        return self.__row

    @property
    def column(self) -> int:
        return self.__column
        
    @column.setter
    def column(self, column:int) -> None:
        self.__column:int = column
        
    @row.setter
    def row(self, row:int) -> None:
        self.__row:int = row

    def __repr__(self):
        return f"Position(row={str(self.row)}, column={str(self.column)})"