import pygame
from spill_objekt import Spill_objekt
from menneske import Menneske
from sau import Sau

class Spillebrett():
    def __init__(self, bredde, hoyde) -> None:
      self.hoyde : int = hoyde
      self.bredde : int = bredde
      self.objekter: list[Spill_objekt] = []

      # Alle "ting" i Pygame må ha en surface og en rect
      self.surface = pygame.Surface((self.bredde, self.hoyde))
      self.rect = self.surface.get_rect()

      #Plasserer spillebrettet i (x, y)
      self.rect.topleft = (0,0)

      self.surface.fill("white")

      self.spiller1 = Menneske()
      self.sauer = []
      for i in range (3):
         self.sauer.append(Sau())



    def legg_til_objekt(self, nytt_objekt: Spill_objekt):
       # legger til nytt objekt i listen self.objekter:
       self.objekter.append(nytt_objekt)


    def fjern_objekt(self, objekt: Spill_objekt):
       self.objekter.remove(objekt)
       

    def tegn(self, vindu: pygame.Surface):
       self.spiller1.tegn(self.surface)
       for sau in self.sauer:
          sau.tegn(self.surface)

       #tegner spillbrettets surface i posisjonen til spillbrettets rect på vinduet
       vindu.blit(self.surface, self.rect)
    
