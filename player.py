# Player class - single instanced
# 
# Will be a controllable car!

import pygame


class Player():

    def __init__(self,DISPLAY: pygame.surface.Surface,speed,acceleration,image: str,starting_pos) -> None:
        self.speed = speed
        self.acceleration = acceleration
        self.original_image = pygame.image.load(image)
        self.image = self.original_image
        self.DISPLAY = DISPLAY
        self.angle = 0

        self.rect = self.image.get_rect()
        self.rect.topleft = ((starting_pos[0],starting_pos[1]))
    
    def update(self):
        self.rect = self.image.get_rect()
        self.DISPLAY.blit(self.image,self.rect)

    def turn(self,left:bool):
        if left:
            self.image = pygame.transform.rotate(self.original_image,self.angle+1)
            self.angle+=1
        else:
            self.image = pygame.transform.rotate(self.original_image,self.angle-1)
            self.angle-=1