import random
from spill_objekt import Spill_objekt


class Sau(Spill_objekt):
    def __init__(self) -> None:
        super().__init__("gray")
        self.blir_loeftet: bool = False
        tilfeldig_y = random.randint(50, 550) #variabler uten self. "glemmes" når init-metoden er ferdig
        tilfeldig_x = random.randint(450, 550) #variabler uten self. "glemmes" når init-metoden er ferdig
        self.plassering(tilfeldig_x, tilfeldig_y)

