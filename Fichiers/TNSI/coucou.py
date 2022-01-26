
def exposant(t8):
    """ prend en argument un tableau de 0 et 1 de taille 8
    renvoie l'exposant(un entier en -126 et +127)"""
    res = 0
    for i in range(8):
        res += t8[7-i]*2**i
    return res - 127

def mantisse(t23):
    """ prend en argument un tableau de 0 et 1 de taille 23
    renvoie la mantisse (un nombre flottant python)"""
    

def flottant(t32):
    """prend en argument un tableau de 0 et 1 de taille 32
    renvoie le nombre correspondant"""
    pass
