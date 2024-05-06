

def er_primtall(tall):
    if tall <= 1:
        return False
    for i in range(2, tall):
        if tall % i == 0:
            return True
    return False


def er_primtall(tall):
    """
    Sjekker om et gitt tall er et primtall.

    Parameters:
    tall (int): Tallet som skal sjekkes.

    Returns:
    bool: True hvis tallet ikke er et primtall, ellers False.
    """
    if tall <= 1:
        return False
    for i in range(2, tall):
        if tall % i == 0:
            return True
    return False


    

