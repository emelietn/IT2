import pygame
from pokemon import Pokemon

class Pokedex():
    def __init__(self):
        self.font = pygame.font.SysFont('arial', 40)
        self.liten_font = pygame.font.SysFont('arial', 20)
        self.title = self.font.render('My Game', True, (255, 255, 255))

    def tegn_start_meny(self, vindu, x):
        if x == 0:
            surface_1 = self.font.render("Se pokemon liste", True, "black", "gray")
            surface_2 = self.font.render ("Avslutt", True, "black")
        elif x == 1:
            surface_1 = self.font.render("Se pokemon liste", True, "black")
            surface_2 = self.font.render ("Avslutt", True, "black", "gray")

        vindu.blit(surface_1,(150,120))
        vindu.blit(surface_2,(150,175))

        

    def pokemon_liste(self, vindu, n, pokemon_liste, x):
        if x == 0:
            pokemon_surface_1 = self.font.render(pokemon_liste[n].print_pokemon_navn(), True, "black", "grey")
            pokemon_surface_2 = self.font.render(pokemon_liste[n + 1].print_pokemon_navn(), True, "black")
            pokemon_surface_3 = self.font.render(pokemon_liste[n + 2].print_pokemon_navn(), True, "black")
            pokemon_surface_4 = self.font.render(pokemon_liste[n + 3].print_pokemon_navn(), True, "black")
        elif x == 1:
            pokemon_surface_1 = self.font.render(pokemon_liste[n].print_pokemon_navn(), True, "black")
            pokemon_surface_2 = self.font.render(pokemon_liste[n + 1].print_pokemon_navn(), True, "black", "gray")
            pokemon_surface_3 = self.font.render(pokemon_liste[n + 2].print_pokemon_navn(), True, "black")
            pokemon_surface_4 = self.font.render(pokemon_liste[n + 3].print_pokemon_navn(), True, "black")
        elif x == 2:
            pokemon_surface_1 = self.font.render(pokemon_liste[n].print_pokemon_navn(), True, "black")
            pokemon_surface_2 = self.font.render(pokemon_liste[n + 1].print_pokemon_navn(), True, "black")
            pokemon_surface_3 = self.font.render(pokemon_liste[n + 2].print_pokemon_navn(), True, "black", "gray")
            pokemon_surface_4 = self.font.render(pokemon_liste[n + 3].print_pokemon_navn(), True, "black")
        elif x == 3:
            pokemon_surface_1 = self.font.render(pokemon_liste[n].print_pokemon_navn(), True, "black")
            pokemon_surface_2 = self.font.render(pokemon_liste[n + 1].print_pokemon_navn(), True, "black")
            pokemon_surface_3 = self.font.render(pokemon_liste[n + 2].print_pokemon_navn(), True, "black")
            pokemon_surface_4 = self.font.render(pokemon_liste[n + 3].print_pokemon_navn(), True, "black", "gray")

        vindu.blit(pokemon_surface_1, (150,120))
        vindu.blit(pokemon_surface_2, (150,175))
        vindu.blit(pokemon_surface_3, (150,225))
        vindu.blit(pokemon_surface_4, (150,275))

    
    def vis_pokemon(self,vindu, n, pokemon_liste, x):
        navn = self.font.render(pokemon_liste[n + x].print_pokemon_navn(), True, "black")
        HP = self.liten_font.render("HP:  " +str(pokemon_liste[n + x].HP), True, "black")
        attack = self.liten_font.render("Attack: " +str(pokemon_liste[n + x].attack), True, "black")
        defence = self.liten_font.render("Defense: "+str(pokemon_liste[n + x].defence), True, "black")
        sp_attack = self.liten_font.render("SP Attack: " +str(pokemon_liste[n + x].sp_attack), True, "black")
        sp_defence = self.liten_font.render("SP Defense: " +str(pokemon_liste[n + x].sp_defence), True, "black")
        bilde = pygame.image.load(pokemon_liste[n + x].bilde)
        bilde: pygame.Surface = pygame.transform.scale(bilde, (100, 100))
        vindu.blit(navn, (150,120))
        vindu.blit(HP, (150, 170))
        vindu.blit(attack, (150, 195))
        vindu.blit(defence, (150, 220))
        vindu.blit(sp_attack, (150, 245))
        vindu.blit(sp_defence, (150, 270))
        vindu.blit(bilde, (290,170))




