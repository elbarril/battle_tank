from tkinter import PhotoImage
from constants import IMAGE_FILE_EXTENSION, IMAGES_PATH

class Image(PhotoImage):
    def __init__(self, filename:str):
        self.__file = IMAGES_PATH + filename + IMAGE_FILE_EXTENSION
        super().__init__(file=self.__file)