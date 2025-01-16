import sys
import pygame

class BlueSkyGame:
    """Class to manage game assets."""
    def __init__(self):
        """Initialize game and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky Game")
        self.clock = pygame.time.Clock()
        self.bg_color = (40, 44, 52)

    def run_game(self):
        """Starts the main loop for game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    bsg = BlueSkyGame()
    bsg.run_game()