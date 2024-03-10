class Size:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
    
    def __str__(self):
        return f"Size(width={self.width}, height={self.height})"