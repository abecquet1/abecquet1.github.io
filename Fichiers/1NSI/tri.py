from random import *
from time import *


### Tri par selection (programme 14) ###
   
def echange(t, i, j):
    """échange les cases d'indices i et j de t"""
    #à compléter

def tri_selection(t):
    """trie t par selection"""
    #à compléter


### Tri par insertion (programme 15) ###

def insere(t, i, v):
    """insère v dans t[0...i[ supposé trié"""
    #à compléter
    
def tri_insertion(t):
    """trie le tableau t par insertion"""
    #à compléter

        
### Tests ###

def tri_python(t):
    t.sort()

def test_correction(f_tri, t):
    """teste la correction de f_tri sur t supposé trié"""
    t1 = []
    for x in t:
        t1.append(x)
    shuffle(t1)
    f_tri(t1)
    return t==t1

def test_correction_alea(f_tri, n):
    """teste la fonction f_tri sur un tableau aléatoire de taille n"""
    t = []
    x = 0
    for i in range(n):
        x += randint(0,10)
        t.append(x)
    return test_correction(f_tri, t)

def test_temps(f_tri, t):
    """trie le tableau t et renvoie le temps d'exécution"""
    tps1 = clock()
    f_tri(t)
    tps2 = clock()
    return tps2-tps1
    
def test_temps_alea(f_tri, n):
    """crée et trie un tableau aléatoire de taille n à l'aide de la fonction f_tri puis renvoie le temps d'exécution"""
    t = []
    for i in range(n):
        t.append(randint(0,n))
    return test_temps(f_tri, t)






























