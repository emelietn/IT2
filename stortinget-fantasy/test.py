import os
import platform
 
def rens_terminal():
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")
 
 
while True:
    rens_terminal()
    print("-- Stortinget-fantasy --")  
    print("1: Politikeroversikt")
    print("2: Avslutt")
    brukervalg = input(">")
 
    if brukervalg == "1":
        print("-- Politikeroversikt --")
        input("Trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "2":
        print("Avslutter..")
        break # bryter ut av while-løkken
    else:
        print("Ugyldig valg")
 