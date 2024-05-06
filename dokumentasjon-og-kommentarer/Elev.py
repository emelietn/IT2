class Elev:

    """
    En klasse for elever på VGS

    attributter
        navn(str) : navnet til eleven
        alder(str): alder til eleven
        klasse(sts): bokstavklasse til eleven(eks: STD)
        fag(list[str]): en liste med fagene eleven tar

    metoder
        legger_til_fag(fag: str): legger til et fag til i faglisten
        fjerner_fag(fag:str): fjerner et fag fra listen
        vis_info(): printer info om elev
    """
    def __init__(self, navn: str, alder: str, klasse: str) -> None:
        self.navn: str = navn
        self.alder: str = alder
        self.klasse: str = klasse
        self.fag: list[str] = []
    def legg_til_fag(self, fag: str):
        self.fag.append(fag)
    
    def fjern_fag(self, fag: str):
        self.fag.remove(fag)
    
    def vis_info(self):
        print(f"{self.navn} ({self.alder})")



meg_selv = Elev("Emelie", 18, "STD")