from character import Character
from enemy import Enemy
from pickup import Pickup

class Pacman(Character):
    pacman = 9
    
    def __init__(self, x, y, images, speed = 1, direction = 'Left'):
        Character.__init__(self, x, y, speed, direction)
        self.score, self.lives, self.level = 0, 3, 1
        self.last_direction, self.next_direction = 'Left', None
        self.invulnerable, self.death = False, False
        self.direction_image(images)
        self._startingPoint = (x, y)

        # https://stackoverflow.com/questions/28518072/play-animations-in-gif-with-tkinter

    def restart_level(self):
        ''' On death, original values are restored. '''
        self.x, self.y = self._startingPoint
        self.change_direction('Left')
        self.next_direction = None
    
    # Game Progression Functions #
    def contact(self, gameObj):
        ''' Updates Pacman's score when he comes into contact with another
            game object, but also handles the two special cases if it's a
            boost pickup, and if it's an enemy. '''

        if type(gameObj) == Pickup:
            if gameObj.boost:
                self.score += 50
                self.invulnerability()
            else:
                self.score += 10
            
        elif type(gameObj) == Enemy:
            if self.invulnerable:
                self.score += 100

            else:
                self.death = True
    
    def level_up(self, score, lives, level) -> None:
        self.score, self.lives, self.level = score, lives, level

    def respawn(self, images):
        self.restart_level()
        self.direction_image( images )
        self.death = False

    def lose_life(self):
        self.lives -= 1
    
    def invulnerability(self):
        self.invulnerable = not self.invulnerable
        
    def out_of_lives(self):
        return self.lives == 0

    # Direction Functions #
    def change_direction(self, direction):
        self.last_direction = self.direction
        self.direction = direction
    
    def has_upcoming_direction(self):
        return self.next_direction is not None
        
    def crossed_boundary(self):
        if self.direction == 'Left':
            self.change_location(27, 14)
        else:
            self.change_location(0, 14)

    # Display Functions #
    def display_score(self) -> str:
        return f'Score: {self.score}'

    def display_lives(self) -> str:
        return f'Lives: {self.lives}'

    def display_level(self) -> str:
        return f'Level: {self.level}'
    
    def direction_image(self, images):
        if self.direction == 'Left':
            self._image = images.return_image('pacmanL')

        elif self.direction == 'Right':
            self._image = images.return_image('pacmanR')

        elif self.direction == 'Down':
            self._image = images.return_image('pacmanD')

        elif self.direction == 'Up':
            self._image = images.return_image('pacmanU')
