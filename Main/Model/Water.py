from Main.Model.Static import Static

class Water(Static):
    def __init__(self, column:int, row:int):
        super().__init__(column, row, is_solid=False)

    def __str__(self):
        return "~"