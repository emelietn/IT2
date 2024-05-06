import pygame
class Spill_objekt():
    def __init__(self, farge: str) -> None:
        self.surface = pygame.Surface((50, 50)) #lager et pygame surface som er 50px bredt og 50pc høyt
        self.rect = self.surface.get_rect() # lager en rect som ligger rundt surface-en
        self.surface.fill(farge)

    def plassering(self, x: int, y: int):
        self.rect.center = (x,y)

    def flyt(self, dx: int, dy: int):
        self.rect.move_ip(dx, dy) #flytter rect-en, bruk move_ip (in place), ikke move

    def tegn(self, vindu: pygame.surface):
        vindu.blit(self.surface, self.rect)

    

    