import pygame

class Ship:
    """Initialize the ship and set it's starting position."""

    def __init__(self, ss_game):
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # Load the ship image and its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the center right of screen.
        self.rect.midleft= self.screen_rect.midleft

        # Store a float for the ship's exact vertical position.
        self.y = float(self.rect.y)

        # Movement flag; start with motionless ship
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the ship position on movement flag."""
        # Update the ship's t value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        # Update rect object from self.y
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)