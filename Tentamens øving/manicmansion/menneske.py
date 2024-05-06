from spill_objekt import Spill_objekt


class Menneske(Spill_objekt):
    def __init__(self) -> None:
        super().__init__("green")
        self.fart_x : int 
        self.fart_y : int
        self.poeng : int
        self.baerer_sau : bool = False
        self.plassering(75, 300)
    

    def beveg(self, ):
        if self.baerer_sau:
            self.flytter(self.fart_x * 0.8, self.fart_y *0.8)
        else:
            self.flytt(self.fart_x, self.fart_y)

        
