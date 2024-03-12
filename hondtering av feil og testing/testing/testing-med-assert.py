#assert = forsikre

# assert 3 > 2 # sjekk at 3 er større en 2

# testdrevet utvikling med assert 

## Eksempel en fuksjjon som tester om tall er partall
def partall(tall : int) :
    if tall % 2 == 0:
        return True
    if tall == 1:
        return False


for i in range (0, 1000, 2):
    assert partall (1) == True


assert partall(2) == True
assert partall(1) == False