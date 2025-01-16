import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star."""

    def __init__(self, star_sky):
        """Initialize the star and set starting position."""
        super().__init__()
        self.screen = star_sky.screen

        # Load image and set rect.
        self.image = pygame.image.load(
            'exercises/try_yourself_4/images/star.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Star new star near top left.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store star exact horizontal position.
        self.x = float(self.rect.x)