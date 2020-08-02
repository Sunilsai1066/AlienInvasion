import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """A class to manage bullets fired from ship"""
    def __init__(self,ai_game):
        """create a bullet object at ship current position"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color

        #create a bullet rect and set correct position
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop

        #store bullet position at decimal value
        self.y=float(self.rect.y)

    def update(self):
        """Move bullet up to screen"""
        #upadte decimal position of bullet
        self.y-=self.settings.bullet_speed
        #update the rect position
        self.rect.y=self.y

    def draw_bullet(self):
        """Drawing bullet to screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
