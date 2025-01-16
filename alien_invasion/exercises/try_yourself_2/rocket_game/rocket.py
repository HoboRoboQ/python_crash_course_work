import pygame

class Rocket:
    """A class to manage the rocket."""

    def __init__ (self, r_game):
        self.screen = r_game.screen
        self.settings = r_game.settings
        self.screen_rect = r_game.screen.get_rect()

        # Load the sip image and get its rect.
        self.image = pygame.image.load(
            'exercises/try_yourself_2/images/rocket.bmp')
        self.image = pygame.transform.scale(self.image, (163, 338))
        
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for ship's exact positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movements flag; start with motionless ship.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship position on movement flag."""
        #update the ship's x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        
        # update rect object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)