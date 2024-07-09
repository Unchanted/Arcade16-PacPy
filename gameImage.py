from PIL.ImageTk import PhotoImage
from pathlib import Path

import os

class GameImage():

    def __init__(self):
        self.start_directory = os.getcwd()
        self.image_directory = Path('.')/"images"
        self.game_images = dict()
    
        for image in self.image_directory.iterdir():
            self.game_images[ image.name.split('.')[0] ] = PhotoImage(file=image)

    def return_image(self, image):
        return self.game_images[image]

    
