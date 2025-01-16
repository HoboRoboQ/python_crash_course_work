import sys
import pygame
from settings import Settings
from morrigan import Morrigan

class MorriganGame:
    """Class to manage game assets."""
    def __init__(self):
        """Initialize game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Morrigan Game")
        self.clock = pygame.time.Clock()
        self.morrigan = Morrigan(self)
        

    def run_game(self):
        """Starts the main loop for game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.morrigan.blitme()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    mg = MorriganGame()
    mg.run_game()