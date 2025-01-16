import sys
import pygame
from settings import Settings
from rain import Rain

class RainDrops:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                              self.settings.screen_height))
        pygame.display.set_caption("Raindrops")

        self.raindrops = pygame.sprite.Group()

        self._create_rain()

    def run_game(self):
        """Start the main loop."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _create_rain():
        """Create a rainy sky."""
        rain = Rain(self)