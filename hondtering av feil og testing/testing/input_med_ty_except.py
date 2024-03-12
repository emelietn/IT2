# OPPGAVE 3.13

# Et progra som fortsetter helt til bruker har skrevet riktig input

# oppretter en variabel år som får veriden 2024
år = 2024

# En uendelig while-løkke som fortsetter å kjøre til break blir kalt
while True:
    try: 
        # Brukeren blir bedt om å oppgi alder, og verdien blir konvertert til et heltall
        alder = int(input("Hvor gammel blir du i år?")) # setter alder til å være lik input til brukeren
        break # Avslutter while-løkken hvis input fungerer
    except:
         # Hvis det oppstår en feil (f.eks. hvis brukeren ikke oppgir et tall), blir det gitt en feilmelding
        print("Ugyldig input. Input må være et tall")


# Beregner fødselsåret ved å subtrahere alder fra gjeldende år
fødselsår = år - alder

# Skriver ut resultatet med bruk av f-string 
print(f"Du er født i {fødselsår}")


# OPPGAVE 3.14

while True:
    try:
        navn = input("Hva er fornavnet og etternavnet dit?")
        break
    except: 
        print("Ugyldig input. Input må være en string")



splittet_navn = navn.split(" ")
antall_navn = len(splittet_navn)
mail = f"{splittet_navn[0].lower()}{splittet_navn[-1][0].lower()}@afk.no"
print(f"Generert e-postadresse: {mail}")


"""
Lag et program som genrerer mailadresser fra fornavn og etternavn. Mailen skal bestå av hele det første fornavnet
og første bokstav i etternavnet etterfulgt av @afk.no. For eksempel skal Thor Christian Coward bli thorc@afk.no. 
Som input til programmet må brukeren skrive inn minst to navn (fornavn og etternavn), hvis ikke skal brukeren få en feilmelding
og få lov til å skrive input på nytt.
"""

while True:
    navn = input("HVa heter du") # -> Emelie Tiril nyiredy
    splitta_navn = navn.splitt(" ") # ["emelie", "Tiril", "Nyiredy"]
    antall_navn = len(splitta_navn)

    if antall_navn < 2:
        print("Ugyldig input. Input må bestå av minst to navn.")
    else:
        break # Bryter ut av løkka

fornavn = splittet_navn[0]
første_bokstav_ettenavn = splitta_navn[-1][0]
mail = fornavn + første_bokstav_ettenavn + "@viken.no"

