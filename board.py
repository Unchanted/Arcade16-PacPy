from pacman import Pacman
from pickup import Pickup
from enemy import Enemy
from wall import Wall


# Just Testing with a basic board at first
def create_board():
    ''' Sets up the board with the numbers, that will represent the objects'''
    new_board = \
    [ [0 for i in range(28)],
      [0, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1, 0],
      [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
      [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)],
      [0 for i in range(28)]]

    # 0 is a Wall object
    # 1 is a Pickup object,
    # 9 is a Pacman object

    # There will be more objects, but until we have movement, we are just testing it through a small border at first

    # Idea
    # 2 will be Pickup objects with Boost == True
    # 3, 4, 5, 6 will be the four enemies with different attributes
    
    return new_board

class Board():

    def __init__(self, width, height, border):
        self._window_width = width
        self._window_height = height
        self._window_border = border

        self.Gamestate = create_board()
        self.gameObjects = set()
        self.pacmanLocation = None
        
    def new_level(self):
        ''' Called when a new level is needed. Alters the Gamestate (which consist of numbers)
            to consist of Pacman game objects. Then updateObjects() is called to fill the
            gameObjects set with all the objects that are on the board. And the initial location
            of Pacman is set. '''
        self.Gamestate = self._pacmanBoard( self.square_height(), self.square_width() )
        self.updateObjects()
        self.pacmanLocation = self.findPacman()

            
    def updateGamestate(self, x, y):
        self.Gamestate[x][y] = self.pacmanLocation

        if self.pacmanLocation.direction == 'Left':
            self.Gamestate[x][y+1] = None

        elif self.pacmanLocation.direction == 'Right':
            self.Gamestate[x][y-1] = None

        elif self.pacmanLocation.direction == 'Down':
            self.Gamestate[x-1][y] = None

        elif self.pacmanLocation.direction == 'Up':
            self.Gamestate[x+1][y] = None
