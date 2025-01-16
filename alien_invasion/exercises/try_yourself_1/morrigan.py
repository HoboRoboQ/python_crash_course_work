import pygame

class Morrigan:
    """Class to manage the character Morrigan."""

    def __init__(self, m_game):
        """Initiates the character and sets starting position."""
        self.screen = m_game.screen
        self.screen_rect = m_game.screen.get_rect()

        self.image = pygame.image.load(
            'exercises/images/Morrigan(Darkstalkers).bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw character at current position."""
        self.screen.blit(self.image, self.rect)