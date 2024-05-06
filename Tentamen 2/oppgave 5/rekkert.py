import pygame

class Rekkert:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)
 
    def beveg(self, dy):
        self.rect.y += dy
        self.rect.y = max(0, min(self.rect.y, 800 - self.rect.height))