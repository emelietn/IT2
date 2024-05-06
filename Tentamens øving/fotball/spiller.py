class Spiller():
    def __init__(self, navn) -> None:
        self._navn = navn
        self._antall_kamper = int

    
    def hent_navn(self):
        return self.navn
    
    def hent_antall_kamper(self):
        return self._antall_kamper
    
    def spill_kamp(self):
        self._antall_kamper += 1

    def sjekk_navn(self, navn):
        spiller = self._navn.split(" ")
        for spiller_navn in spiller:
            if navn in spiller_navn:
                return True
            
        return False
                
            

            
spiller1 = Spiller("Caroline Graham Hansen")
print(spiller1.sjekk_navn("Karoline"))
