import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class for managing ship"""
    def __init__(self,ai_game):
        """Initilizing attributes an dstarting position"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        self.moving_right=False
        self.moving_left=False

        #Load the ship image and get its rect
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()

        #Start each new ship at bottom of screen
        self.rect.midbottom=self.screen_rect.midbottom

        #Store a decimal for ship horizontal position
        self.x=float(self.rect.x)

    def update(self):
        """Update the ship movement based on flag"""
        """Update ship x value not rect value"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed

        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed

        """update rect object from self.x"""
        self.rect.x=self.x



    def blitme(self):
        """Draw the ship at it's current loaction"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
