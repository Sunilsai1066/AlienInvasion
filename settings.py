class Settings:
    """A Class to store all game settings"""
    def __init__(self):
        """Initializing game settings"""
        #Screen settings
        self.screen_width=1200#1366
        self.screen_height=600#713
        self.bg_color=(230,230,230)
        #Ship settings
        self.ship_speed=1.8
        self.ship_limit = 3
        #Bullet Settings
        self.bullet_speed=1.0
        self.bullet_speed = 1.5
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3
        #Alien Settings
        self.alien_speed=1.0
        self.fleet_drop_speed=10
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction=1

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        """Increases Alien Points for each level"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        #To check point increase fro each level uncomment below line
        #print(self.alien_points)

