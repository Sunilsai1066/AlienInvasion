import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """Class to represent single alien of fleet"""
    def __init__(self,ai_game):
        """Install alien and give start position"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        #Load alien image
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        #start new alien at top left corner
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #storing alien's exact horizontal position
        self.x=float(self.rect.x)

    def check_edges(self):
        """Returns true if alien touches edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True

    def update(self):
        """Move ALien To Right"""
        self.x+=(self.settings.alien_speed*self.settings.fleet_direction)
        self.rect.x=self.x



