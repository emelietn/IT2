from spiller import Spiller

class Lag():
    def __init__(self, navn) -> None:
        self._navn = navn
        self._spillere = []
        self._seier = 0
        self._uavgjort = 0
        self._tap = 0

    
    def hent_navn(self):
        return self._navn
    
    def hent_poeng(self):
        poeng = self._seier * 3 + self._uavgjort * 1 + self._tap * 0
        return poeng
    
    def legg_til_spiller(self, spiller: Spiller):
        self._spillere.append(spiller)


    def spill_kamp(self):
        for spiller in self._spillere:
            spiller.spill_kamp()

    def seier(self):
        self._seier += 1
        self.spill_kamp()

    def uavgjort(self):
        self._uavgjort += 1
        self.spill_kamp()

    def tap(self):
        self._tap += 1
        self.spill_kamp()

    def finn_spiller(self, navn: str):
        for spiller in self._spillere:
            if spiller.sjekk_navn(navn) == True:
                return spiller
        return None
    
    



