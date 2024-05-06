import pygame
import random

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(800 // 2, 600 // 2, 10, 10)
        self.tilbakestill()
 
    def tilbakestill(self):
        self.rect.center = (800 // 2, 600 // 2)
        self.speed = [random.choice([-3, 3]), random.choice([-3, 3])]
 
    def oppdater(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed[1] = -self.speed[1]
        if self.rect.left <= 0 or self.rect.right >= 800: # Sjekker kollisjon med venstre og høyre side
            self.speed[0] = -self.speed[0]
 
    def treffer_rekkert(self, rekkert):
        return self.rect.colliderect(rekkert.rect)