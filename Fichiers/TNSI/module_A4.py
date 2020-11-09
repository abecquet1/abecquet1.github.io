from random import randint

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
    """affiche les noeuds de a en suivant un parcours postfixe (gauche, droite, valeur)"""
    if not(a is None) :
        parcours_postfixe(a.gauche)
        parcours_postfixe(a.droite)
        print(a.valeur)

def creer_ABR():
    """renvoie un arbre vide"""
    return None

def insertion_ABR(a, v):
    """renvoie un ABR copie de a dans laquelle on a inséré à valeur x"""
    if a is None:
        return Noeud(None, v, None)
    elif v<a.valeur:
        return Noeud(insertion_ABR(a.gauche,v), a.valeur, a.droite)
    else:
        return Noeud(a.gauche, a.valeur, insertion_ABR(a.droite,v))

def recherche_ABR(a,v):
    """teste si la valeur x est présente dans l'ABR a"""
    if a is None:
        return False
    elif a.valeur == v:
        return True
    elif a.valeur>v:
        return recherche_ABR(a.gauche,v)
    else:
        return recherche_ABR(a.droite,v)

class ABR:
    def __init__(self):
        self.arbre = None

    def add(self, x):
        self.arbre = insertion_ABR(self.arbre, x)

    def __contains__(self,x):
        return recherche_ABR(self.arbre, x)

    def affiche(self):
        parcours_infixe(self.arbre)

        
### TESTS ####
a = ABR()
for i in range(5):
    a.add(randint(1,100))
print("Attendu : 5 nombres aléatoires triés")
a.affiche()
print()
print("Attendu : 5 nombres aléatoires triés et 13 à la bonne place")
a.add(13)
a.affiche()

print()
print("Attendu : True, False, False")
print(13 in a)
print(101 in a)
print(1 in ABR())
    
