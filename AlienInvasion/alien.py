import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('alien2.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)


        '''
        We can call the new method check_edges() on any alien to see whether
        it’s at the left or right edge. The alien is at the right edge if the right attribute
        of its rect is greater than or equal to the right attribute of the screen’s
        rect. It’s at the left edge if its left value is less than or equal to 0.
        '''
    def check_edges(self): # Checking Whether an Alien Has Hit the Edge
        """Return True if alien is at edge of screen."""

        screen_rect = self.screen.get_rect()
        if screen_rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


    def update(self):
        """Move the alien to the right."""
        self.x += self.settings.alien_speed
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x