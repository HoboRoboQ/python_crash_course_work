class Settings:
    """A class to store all the settings for Rocket Game."""

    def __init__ (self):
        """Initialize the game settings."""
        # Screen Settings
        self.screen_width = 800
        self.screen_height = 1200
        self.bg_color = (0, 0, 0)

        # Rocket settings
        self.rocket_speed = 2