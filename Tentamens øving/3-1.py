def lag_brukernavn(navn):
    navn = navn.split(" ")
    navn = navn[0] + navn[1][0]
    navn = navn.lower()
    return navn
    
print(lag_brukernavn("Emelie Nyiredy"))

def lag_epost(navn, skole):

    epost = lag_brukernavn(navn) + "@" + skole.lower() + "viken.no"
    return epost

print(lag_epost("Emelie Nyiredy", "Sandvika"))

def fjern_falske_brukere(brukernavn, nøkkelord):
    for navn in brukernavn:
        if nøkkelord in navn:
            brukernavn.remove(navn)
            return brukernavn
        
print(fjern_falske_brukere(["thorc", "ravim", "celiliet", "fredrikg"], "fred"))
