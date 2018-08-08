


import pygame
import time
import random
from pygame.locals import *
from spritedefs import EnvSprite, NPCSprite
import os
from spriteimages import TextImgs

pygame.init()
cwd = os.getcwd()
from spriteimages import CharacterImgs as chImg
from spritedefs import Animation

class PeonNPC(NPCSprite):

    def __init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, IDNum):
        collisionWidth = 48
        collisionHeight = 30
        attackWidth = 48
        attackHeight = 100
        self.img = pygame.image.load(chImg.standing)
        self.health = 100
        self.minusTen = pygame.image.load(TextImgs.minusTen)
        self.size = tuple([i * zoom for i in self.minusTen.get_rect().size])
        self.IDNum = IDNum
        self.hit = False
        self.spriteType = "NPC"
        self.hitAnimaitonCounter = 0
        self.walkRightAnimation = Animation(chImg.walkRightArray, 5)
        self.walkLeftAnimation = Animation(chImg.walkLeftArray, 5)
        self.walkUpAnimation = Animation(chImg.walkUpArray, 5)
        self.walkDownAnimation = Animation(chImg.walkDownArray, 5)
        NPCSprite.__init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, collisionWidth, collisionHeight, attackWidth, attackHeight)


    def updateAnimation(self, display):
        if self.hit:
            self.hitAnimaitonCounter += 1
            display.blit(self.minusTen, (self.x, self.y - self.hitAnimaitonCounter * 2))

            if self.hitAnimaitonCounter == 10:
                self.hitAnimaitonCounter = 0
                self.hit = False

        if self.direction == 'up':
            self.walkUpAnimation.update()
            self.img = self.walkUpAnimation.img()
        if self.direction == 'down':
            self.walkDownAnimation.update()
            self.img = self.walkDownAnimation.img()
        if self.direction == 'right':
            self.walkRightAnimation.update()
            self.img = self.walkRightAnimation.img()
        if self.direction == 'left':
            self.walkLeftAnimation.update()
            self.img = self.walkLeftAnimation.img()

        self.img = pygame.transform.scale(self.img, self.size)
