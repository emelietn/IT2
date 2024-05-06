import pygame

class Hinder:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 20)
 
    def tegn(self, vindu):
        pygame.draw.rect(vindu, "white", self.rect)
 
    def treffer_ball(self, ball):
        return self.rect.colliderect(ball.rect)