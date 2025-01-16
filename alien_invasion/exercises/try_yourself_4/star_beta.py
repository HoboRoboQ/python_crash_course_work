import sys
import pygame
from settings import Settings
from star import Star
from random import randint

class StarScreen:
    """Overall class to manage assets."""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                              self.settings.screen_height))
        pygame.display.set_caption("Star Screen")
        
        self.stars = pygame.sprite.Group()

        self._create_sky()

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
    
    def _create_sky(self):
        """Create a stary sky."""
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = 2 * star_width, 2 * star_height
        while current_y < (self.settings.screen_height - 3 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width

            # Finish a row; reset x value and increment y value.
            current_x = star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        """Create a star and place it in the sky"""
        new_star = Star(self)
        new_star.rect.x = x_position + self._get_star_offset()
        new_star.rect.y = y_position + self._get_star_offset()

        self.stars.add(new_star)

    def _get_star_offset(self):
        """Return random adjustment to a star's position."""
        offset_size = 30
        return randint(-1 * offset_size, offset_size)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    star_sky = StarScreen()
    star_sky.run_game()