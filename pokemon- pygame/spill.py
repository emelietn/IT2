# 1. oppsett
import pygame
import json
from pokemon import Pokemon

with open("pokemon.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
pokemon = data


pokemon_liste = []
for pokemon_ordbok in data:
    ny_pokemon = Pokemon(pokemon_ordbok)
    pokemon_liste.append(ny_pokemon)


#initialiserer pygame
pygame.init()

# Definerer spillvinduets bredde, høyde og bildefrekvens per sekund (FPS)
BREDDE = 400
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

         

pokemon_font = pygame.font.SysFont("Arial", 16)
pokemon_info_surface = pokemon_font.render(pokemon_liste[0].print_pokemon_navn(), True, "black")




while True:
    #2.hondter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            pygame.quit()
            raise SystemExit
    

        
# 3. oppdater
# 4. tegn   
    vindu.fill("white")
    vindu.blit(pokemon_info_surface, (0,0))
  

    pygame.display.flip()
    klokke.tick(FPS) 

