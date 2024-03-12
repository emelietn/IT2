import os
import platform
import json
from politiker import Politiker

 
def rens_terminal():
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")
 
 #1 oppsett
# åpner json fila og putter alt inholde inn i variabelen data
with open("politiker.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
representanter = data["dagensrepresentanter_liste"] # henter ut lista med representanter

#oppretter en liste med politiker_ objeter ( objekter av klassen politiker )
politikere = []
for politiker_ordbok in representanter:
    ny_politiker = Politiker(politiker_ordbok)
    politikere.append(ny_politiker)
 
while True:
    rens_terminal()
    print("-- Stortinget-fantasy --")  
    print("1: Politikeroversikt")
    print("2: Avslutt")
    brukervalg = input(">")

    if brukervalg == 1:
        print("politikeroversikt")
        for politiker in politikere:
            print(politiker)
        input("Trykk ente for å gå tilbake til hoved menyen")
    elif brukervalg == "2":
        print("Avslutter..")
        break # bryter ut av while-løkken
    else:
        print("ugyldig input")
        input("Trykk enter for å gå tilbake til hovedmeny")