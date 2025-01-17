class Settings:
    """A class to store all the settings for Side Shooter."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = 3

        # Bullet settings

        self.bullet_speed = 3.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 250, 250)
        self.bullets_allowed = 12