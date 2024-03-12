# Et program som finner fødselsår basert på alder
år = 2024


try: 
    alder = int(input("Hvor gammel blir du i år?"))
    fødselsår = år - alder
    print(f"du er født i {fødselsår}")
except:
    print("Ugyldig input. Input må være et tall")

print(f"koden fortsetter")


# Et anne eksempel

try: 
    tall = int(input("skriv et tall"))
except: 
    print("ugyldig input. Setter tall til 10")
    tall = 10


print(tall) # tall = 10 hvis brukeren ikke skriver inn et tall i input
