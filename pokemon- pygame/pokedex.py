import pygame
from pokemon import Pokemon

class Pokedex():
    def __init__(self):
        self.font = pygame.font.SysFont('arial', 40)
        self.title = self.font.render('My Game', True, (255, 255, 255))

    def tegn_start_meny(self, vindu):
        vindu.fill("white")
        vindu.blit(self.knapp("Enter Pokedex"),(20, 300))

    def pokemon_liste(self, vindu, n, pokemon_liste):
        vindu.fill("white")
        pokemon_surface_1 = self.font.render(pokemon_liste[n].print_pokemon_navn(), True, "black", "pink")
        pokemon_surface_1.backgroundcolor 
        pokemon_surface_2 = self.font.render(pokemon_liste[n + 1].print_pokemon_navn(), True, "black")
        pokemon_surface_3 = self.font.render(pokemon_liste[n + 2].print_pokemon_navn(), True, "black")
        pokemon_surface_4 = self.font.render(pokemon_liste[n + 3].print_pokemon_navn(), True, "black")
        vindu.blit(pokemon_surface_1, (20,40))
        vindu.blit(pokemon_surface_2, (20,80))
        vindu.blit(pokemon_surface_3, (20,120))
        vindu.blit(pokemon_surface_4, (20,160))

