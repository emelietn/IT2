class Pokemon:

    """
    En klasse for Pokemons

    attributter
        navn(str) : navnet til pokemonen
        bilde(str): bilde av pokemonen
        type(list[str]): en liste med elementene pokemonen har
        HP(int): Hit Points til pokemonen
        attack(int): Tall som sier hvor sterk pokemonen er
        defence(int): Tall som sier hvor godt pokemonen klarer å forsvare seg selv
        sp_attack(int): tall som sier hvor fort pokemonen klarer å angripe
        sp_defence(int): Tall som sier hvor raskt pokemonen klarer å forsvare seg selv
        id(int): tall som beskriver hvilken pokemon det er


    metoder
        print_pokemon_navn(): returnerer navnet til pokemonen som en string
        print_pokemon_info(): returnerer en string medinfo til pokemon nedover hverandre

    """
    def __init__(self, pokemon_ordbok : dict) -> None:
        self.navn : str = pokemon_ordbok ["name"]["english"]
        self.bilde : str = "bilder/" + pokemon_ordbok["bilde"]
        self.type : list[str]= pokemon_ordbok ["type"]
        self.HP : int = pokemon_ordbok ["base"]["HP"]
        self.attack : int = pokemon_ordbok ["base"]["Attack"]
        self.defence: int = pokemon_ordbok ["base"]["Defense"]
        self.sp_attack : int = pokemon_ordbok["base"]["Sp. Attack"]
        self.sp_defence : int = pokemon_ordbok["base"]["Sp. Defense"]
        self.speed : int = pokemon_ordbok ["base"]["Speed"]
        self.id : int = pokemon_ordbok ["id"]

    def print_pokemon_navn(self):
        return f" {self.navn}"
    
    
    def print_pokemon_info(self):
        resultat = f""

        for t in self.type:
            resultat += t  + "\n"

        resultat += "HP:" + str(self.HP) + "\n"
        resultat += str(self.atack) + "\n"
        resultat += str(self.defence) + "\n"
        resultat += str(self.sp_attack) + "\n"
        resultat += str(self.sp_defence) + "\n"
        resultat += str(self.speed) + "\n"
        
        return resultat
       
