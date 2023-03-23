from Main.Model.Static import Static

class Stone(Static):
    def __init__(self, column:int, row:int):
        super().__init__(column, row, is_solid=True)

    def __str__(self):
        return "◙"