import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    """Class to manage rain falling."""

    def __init__(self, rd_game):
        """Initialize raindrops and set its starting position."""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        # Load the rain image and set its rect attribute.
        self.image = pygame.image.load(
            'exercises/try_yourself_5/images/rain.bmp')
        self.rect = self.image.get_rect()

        # Star each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact horizontal position.
        self.x = float(self.rect.x)

        