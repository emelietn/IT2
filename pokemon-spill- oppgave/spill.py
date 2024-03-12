# oppgave 3.1

import os
import platform
import json
from pokemon import Pokemon
from trener import Trener
 
def rens_terminal():
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

with open("pokemon.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
pokemon = data


pokemon_liste = []
for pokemon_ordbok in data:
    ny_pokemon = Pokemon(pokemon_ordbok)
    pokemon_liste.append(ny_pokemon)
 
trener_liste = []


 
while True:
    rens_terminal()
    print("-- pokemon spill --")  
    print("1: Se pokemonoversikt")
    print("2: se treneroversikt")
    print("3:Lag trener")
    print("4:Se Avslutt")
    brukervalg = input(">")
 
    if brukervalg == "1":
        print("-- Pokemonoversikt --")
        for pokemon in pokemon_liste:
            print(pokemon.print_pokemon())
        input("Trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "2":
        print("Treneroversikt")
        for trener in trener_liste:
            print(trener.print_trener())
        input("Trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "3":
        print("Lag trener")
        navn = input("Hva heter treneren?") 
        trener_liste.append(Trener(navn))
    elif brukervalg == "9":
        print("Avslutter..")
        break # bryter ut av while-løkken
    else:
        print("Ugyldig valg")




