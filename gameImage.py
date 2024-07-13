from PIL.ImageTk import PhotoImage
from pathlib import Path 

import os

class GameImage():

    def __init__(self):
        ''' Initializes a game image object that holds all the of the images for the game.
            The os library is used to get the current directory, and then iterates
            through all of the images inside the 'images' directory. This makes all of the
            images available from different directories. '''
        self.start_directory = os.getcwd()
        self.image_directory = Path('.')/"images"
        self.game_images = dict()
    
        for image in self.image_directory.iterdir():
            self.game_images[ image.name.split('.')[0] ] = PhotoImage(file=image)

    def return_image(self, image) -> PhotoImage:
        ''' Returns the image from the image_directory given the image argument. '''
        return self.game_images[image]

    
