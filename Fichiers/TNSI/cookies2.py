from math import floor

def fill(base,n):
    cost = [[0 for j in range(n+1-i)] for i in range(n+1)]
    #cost[i][j] = cout de passage de i à i+j unités
    for i in range(n+1):
        cost[i][0] = 0
    cost[0][1] = base
    for i in range(1,n):
        cost[i][1] = cost[i-1][1]*1.15
    for j in range(2,n+1):
        for i in range(n+1-j):
            cost[i][j]=cost[i][j-1]+cost[i+j-1][1]
    return cost


class Unit:
    def __init__(self, name, cps, base, n):
        self.cost_tab = fill(base, n)
        self.name = name
        self.cps = cps
        self.number = 0

    def upgrade(self, factor):
        self.cps *= factor

    def add(self, number):
        self.number += number

    def cost(self, number):
        return self.cost_tab[self.number][number]
        

class Game:
    def __init__(self,n):
        self.unit = []
        self.unit.append(Unit("cursor", 0.1, 15, n))
        self.unit.append(Unit("grandma", 1, 100, n))
        self.unit.append(Unit("farm", 8, 1100, n))
        self.unit.append(Unit("mine", 47, 12000, n))
        self.unit.append(Unit("factory", 260, 130000, n))
        self.unit.append(Unit("bank", 1400, 1.4e6, n))
        self.unit.append(Unit("temple", 7800, 20e6, n))
        self.unit.append(Unit("wizard tower", 44000, 330e6, n))
        self.unit.append(Unit("shipment", 260000, 5.1e9, n))
        self.unit.append(Unit("alchemy lab", 1.6e6, 75e9, n))
        self.unit.append(Unit("portal", 10e6, 1e12, n))
        self.unit.append(Unit("time machine", 65e6, 14e12, n))
        self.cash = 0
        self.cps = 0
        self.click_value = 1

    def update_cps(self):
        self.cps = sum([u.number*u.cps for u in self.unit])
        
    def update_cash(self):
        self.cash += self.cps
    
    def click(self):
        self.cash += self.click_value

    def buy(self, name, number):
        for u in self.unit:
            if u.name == name:
                if u.cost(number)<self.cash:
                    return "Not enough cash to buy "+str(number)+" unité(s) "+name
                else:
                    self.cash -= u.cost(number)
                    u.number += number
                    self.update_cps()
                    return "Achat de "+str(number)+" unité(s) "+name+" effectué"
        return "Unité "+name+" introuvable"
        

        
        

        

g = Game(100)
g.click()
g.click()
print(g.cash)
for i in range(13):
    g.click()
print(g.buy("cursor",1))
g.update_cash()
                                                
            

