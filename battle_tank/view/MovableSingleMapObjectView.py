from view.SingleMapObjectView import SingleMapObjectView, Image
from model.MovableSingleMapObject import MovableSingleMapObject

class MovableSingleMapObjectView(SingleMapObjectView):
    def __init__(self, model:MovableSingleMapObject, images:dict[str,Image]):
        super().__init__(model, images[model.direction])
        self.__model = model
        self.__images = images
    
    @property
    def model(self): return self.__model

    def move(self, direction):
        if self.model.direction != direction:
            self.image = self.__images[direction]
            self.model.direction = direction
        else:
            move_y, move_x = direction
            self.model.position.x += move_x
            self.model.position.y += move_y

    def next_area(self, direction):
        move_y, move_x = direction
        left = self.x0 + move_x
        top = self.y0 + move_y
        right = self.x1 + move_x
        bottom = self.y1 + move_y
        return (left, top, right, bottom)