class Cellule:
    """ classe décrivant les cellules d'une liste chaînée """
    def __init__(self, v, s=None):
        self.valeur = v
        self.suivante = s

def _longueur(cell):
    """ renvoie la longueur de la chaine de cellules"""
    if cell is None:
        return 0
    else:
        return 1+_longueur(cell.suivante)

def _nieme(cell, n):
    """ renvoie la valeur de la n ieme cellule de la chaine"""
    if cell is None:
        raise IndexError("Indice invalide")
    elif n==0:
        return cell.valeur
    else:
        return _nieme(cell.suivante, n-1)

def _concatener(c1,c2):
    """ renvoie la concaténation des deux chaines"""
    if c1 is None:
        return c2
    else:
        return Cellule(c1.valeur, _concatener(c1.suivante,c2))

def _renverser(cell):
    """ renvoie la chaine inversée"""
    res = None
    copie = cell
    while not(copie is None):
        res = Cellule(copie.valeur, res)
        copie = copie.suivante
    return res

def _texte(cell):
    """ revoie une chaine de caractères au format v0, v1, etc.""" 
    if cell is None:
        return ""
    elif cell.suivante is None:
        return  str(cell.valeur)
    else:
        return str(cell.valeur) + " ," + _texte(cell.suivante)

class Liste:
    """ classe liste chainée"""
    def __init__(self):
        self.tete = None

    def est_vide(self):
        """ teste si la liste est vide"""
        return self.tete is None

    def __str__(self):
        """ surcharge de str """
        return '['+_texte(self.tete)+']'

    def ajoute(self, x):
        """ ajoute x en tete de la liste"""
        self.tete = Cellule(x, self.tete)

    def __getitem__(self, n):
        """ surcharge de getitem"""
        return _nieme(self.tete, n)

    def __len__(self):
        """ surcharge de len"""
        return _longueur(self.tete)

    def reverse(self):
        """ renverse la liste par effet de bord """
        self.tete = _renverser(self.tete)

    def __add__(self, lst):
        """ renvoie la concaténation des deux listes"""
        r = Liste()
        r.tete = _concatener(self.tete, lst.tete)
        return r



### Tests ###
"""
print("test des cellules")
cell = Cellule(1, Cellule(2,Cellule(3,None)))
print(_longueur(cell))
print(_nieme(cell,0))
print(_nieme(cell,1))
print(_nieme(cell,2))
print()


print("test des listes")
lst1 = Liste()
lst1.ajoute(12)
lst1.ajoute(42)
lst1.ajoute(23)
print(lst1)
lst2 = Liste()
lst2.ajoute(13)
print(lst1[1])
print(len(lst1))
lst1.reverse()
print(lst1)
print(lst1+lst2)
"""


