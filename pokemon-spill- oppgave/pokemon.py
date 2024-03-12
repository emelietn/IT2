class Pokemon:
    def __init__(self, pokemon_ordbok : dict) -> None:
        self.navn : str = pokemon_ordbok ["name"]["english"]
        self.type : list[str]= pokemon_ordbok ["type"]
        self.HP : int = pokemon_ordbok ["base"]["HP"]
        self.atack : int = pokemon_ordbok ["base"]["Attack"]
        self.defence: int = pokemon_ordbok ["base"]["Defense"]
        self.sp_atack : int = pokemon_ordbok["base"]["Sp. Attack"]
        self.sp_defense : int = pokemon_ordbok["base"]["Sp. Defense"]
        self.speed : int = pokemon_ordbok ["base"]["Speed"]
        self.id : int = pokemon_ordbok ["id"]


    def print_pokemon(self):
        return f"Navn : {self.navn} Type: {self.type}"
    
    
    


