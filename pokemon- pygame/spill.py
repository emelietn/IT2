# 1. oppsett
import pygame
import json
from pokemon import Pokemon
from pokedex import Pokedex

# åpner json filen til pokemon
with open("pokemon.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
pokemon = data


pokemon_liste = []
for pokemon_ordbok in data:
    #lager en ny pokemon
    ny_pokemon = Pokemon(pokemon_ordbok)
    #legger til ny_pokemon i listen med pokemons
    pokemon_liste.append(ny_pokemon)


#initialiserer pygame
pygame.init()
gameboy_bilde = pygame.image.load("bilder/gameboy.jpeg")
gameboy_ny = pygame.transform.scale(gameboy_bilde, (600, 800))

# Definerer spillvinduets bredde, høyde og bildefrekvens per sekund (FPS)
BREDDE = 600
HOYDE = 800
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

spill_tilstand = "start_meny"

         
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
                if x == 3:
                    n += 1
                    if n == len(pokemon_liste) - 4:
                        n = 0
                        x = 0
                elif x < 3:
                    x += 1
               
            elif event.key == pygame.K_UP:
                if x == 0:
                    n -= 1
                else:
                    x -= 1
                    


            elif event.key == pygame.K_RETURN:
                if spill_tilstand == "start_meny":
                    spill_tilstand = "vis_pokemon_liste"
                elif spill_tilstand == "vis_pokemon_liste":
                    spill_tilstand = "vis_pokemon"
            elif event.key == pygame.K_b:
                if spill_tilstand == "vis_pokemon_liste":
                    spill_tilstand = "start_meny"
                elif spill_tilstand == "vis_pokemon":
                    spill_tilstand = "vis_pokemon_liste"

    
    
    taster = pygame.key.get_pressed()

    vindu.blit(gameboy_ny, (0,0))

        
# 3. oppdater
    if spill_tilstand == "start_meny":
        pokedex.tegn_start_meny(vindu, x)
    elif spill_tilstand == "vis_pokemon_liste":
        pokedex.pokemon_liste(vindu, n, pokemon_liste, x)
    elif spill_tilstand == "vis_pokemon":
        pokedex.vis_pokemon(vindu, n, pokemon_liste, x)


# 4. tegn   
        
        

    pygame.display.flip()
    klokke.tick(FPS) 

