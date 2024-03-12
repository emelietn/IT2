from pokemon import Pokemon

class Trener:
    def __init__(self, navn : str) -> None:
        self.navn = navn
        self.pokemon_liste = []


    def legg_til_pokemon(self, pokemon : Pokemon):
        self.pokemon_liste.append(pokemon)

    def fjern_pokemon(self, pokemon : Pokemon):
        self.pokemon_liste.remove(pokemon)

    def print_trener(self):
        return f" Trener : {self.navn} Pokemon: {len(self.pokemon_liste)}"



