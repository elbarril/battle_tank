from tkinter import PhotoImage
from Constants import IMAGE_FILE_EXTNSION

class Image(PhotoImage):
    def __init__(self, image_filename:str):
        super().__init__(file=image_filename + IMAGE_FILE_EXTNSION)