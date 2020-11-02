class Noeud:
    def __init__(self, g, v, d):
        """Un noeud d'un arbre binaire"""
        self.gauche = g
        self.valeur = v
        self.droite = d

def taille(a):
    """renvoie le nombre de noeuds présent dans l'arbre a"""
    if a is None :
        return 0
    else :
        return 1 + taille(a.gauche) + taille(a.droite)

def hauteur(a):
    """renvoie la hauteur de l'arbre a"""
    if a is None :
        return 0
    else :
        return 1 + max(hauteur(a.gauche), hauteur(a.droite))

def parcours_infixe(a):
    """affiche les noeuds de a en suivant un parcours infixe (gauche, valeur, droite)"""
    if not(a is None) :
        parcours_infixe(a.gauche)
        print(a.valeur)
        parcours_infixe(a.droite)

def parcours_prefixe(a):
    """affiche les noeuds de a en suivant un parcours préfixe (valeur, gauche, droite)"""
    if not(a is None) :
        print(a.valeur)
        parcours_prefixe(a.gauche)
        parcours_prefixe(a.droite)

def parcours_postfixe(a):
    "affiche les noeuds de a en suivant un parcours postfixe (gauche, droite, valeur)"""
    if not(a is None) :
        parcours_postfixe(a.gauche)
        parcours_postfixe(a.droite)
        print(a.valeur)


### TESTS ####
        
"""
douze = Noeud(None, 12, None)
trente = Noeud(None, 30, None)
cinq = Noeud(None, 5, None)
deux = Noeud(None, 2, None)
a1 = Noeud(douze, 50, trente)
a2 = Noeud(cinq, 546, deux)
a = Noeud(a1, 321, a2)
b1 = Noeud(douze, 50, trente)
b2 = Noeud(b1, 321, cinq)
b = Noeud(b2, 546, deux)
print("taille a :", taille(a))
print("taille b :", taille(b))
print("hauteur a :", hauteur(a))
print("hauteur b :", hauteur(b))
print("Infixe a :")
parcours_infixe(a)
print("Infixe b :")
parcours_infixe(b)
print("Préfixe a :")
parcours_prefixe(a)
print("Préfixe b :")
parcours_prefixe(b)
print("Postfixe a :")
parcours_postfixe(a)
print("Postfixe b :")
parcours_postfixe(b)
"""
        
