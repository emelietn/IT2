# 1. oppsett
import pygame
import json
from pokemon import Pokemon
from pokedex import Pokedex

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
pokemon_info_surface = pokemon_font.render(pokemon_liste[1].print_pokemon_navn(), True, "black")
pokedex = Pokedex()
n = 0
x = 0



while True:
    #2.hondter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if n < len(pokemon_liste) - 4 and x == 3:
                    n += 1
                elif x < 3:
                    x += 1
            elif event.key == pygame.K_UP:
                n -= 1
        


                

        
    
    taster = pygame.key.get_pressed()

        
# 3. oppdater
# 4. tegn   
    vindu.fill("white")
    vindu.blit(pokemon_info_surface, (0,0))
    pokedex.pokemon_liste(vindu, n, pokemon_liste)
  

    pygame.display.flip()
    klokke.tick(FPS) 

