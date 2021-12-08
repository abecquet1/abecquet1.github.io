from random import randint
from module_A4 import *
from ex81 import minimum


"""
minimum(a)
    Critères d'acceptance de la fonction :
    + elle doit renvoyer le plus petit élément de l'ABR argument

    Cas dégénérés à tester :
    + Arbre vide -> Erreur

    Tests aléatoire :
    + on génère des valeurs aléatoires qu'on insère dans un ABR
    + on calcule séquentiellement le minimum de ces valeur au fur et à mesure
    + on confronte ce minimum au résultat de la fonction
"""


def test_minimum():
    a = None
    try:
        minimum(a)
        err = 0
    except IndexError:
        err = 1
    assert err == 1, "Attention : l'arbre vide ne déclenche pas d'erreur !"   
    for i in range(10):
        a = creer_ABR()
        mini = 1000
        for j in range(10):
            x = randint(1,1000)
            if x<mini:
                mini=x
            a = insertion_ABR(a,x)
        assert minimum(a) == mini, "Attention : un arbre ne convient pas ! !"   
    print("All good !")










