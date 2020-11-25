from math import *
from tkinter import *

#Constants
H = 1050
W = 1680
ECHELLE = 1600000000
G = 9.67408e-11
DT = 36000
SLEEP = 5

#Planet class
class Planet:
    def __init__(self, name, mass, radius, color, x, y, vx, vy, can):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.can = can
        self.picture = can.create_oval(W/2+(x-radius)/ECHELLE, H/2+(y-radius)/ECHELLE,W/2+(x+radius)/ECHELLE, H/2+(y+radius)/ECHELLE, fill = color)

    def accelerate(self, dt, a):
        """make the planet accelerate according to a acceleration vector a=(ax, ay)"""
        ax, ay = a
        self.vx = self.vx+ax*dt
        self.vy = self.vy+ay*dt

    def move(self, dt):
        """make the planet move according to its velocity vector """
        self.x = self.x+self.vx*dt
        self.y = self.y+self.vy*dt
        self.can.move(self.picture, self.vx*dt/ECHELLE, self.vy*dt/ECHELLE)
        
    def field(self,x,y):
        """returns the gravitationnal field of the planet""" 
        d = sqrt((x-self.x)**2+(y-self.y)**2)
        if d==0:
            return 0,0
        gx = -(x-self.x)*G*self.mass/d**3
        gy = -(y-self.y)*G*self.mass/d**3
        return gx, gy



def deplacement():
    def g(x,y):
        gx = 0
        gy = 0
        for p in system:
            gx+=p.field(x,y)[0]
            gy+=p.field(x,y)[1]
        return gx,gy  
    for p in system:
        p.accelerate(DT, g(p.x,p.y))
    for p in system:
        p.move(DT)
    root.after(SLEEP,deplacement)


#Tkinter initialisation
root = Tk()
root.title("Gravitation")
can = Canvas(root, height = H, width = W, bg = 'black')

#planets creation
soleil = Planet("Sun", 2e30, 696342000, 'white', 0,0,0,0, can)
mercure = Planet("Mercury", 3e23, 2439000, 'red', 50597870700, 0,0,35000*1.8,can)
venus = Planet("Venus", 5e24, 6000000, 'grey', 108000000000,0,0,24000*1.8, can)
terre = Planet("Earth", 6e24, 6400000, 'blue', 149597870700, 0, 0, 20000*1.8, can)
mars = Planet("Mars", 6e23, 3400000, 'red', -230655000000,0,0,-20000*1.5, can)
jupiter = Planet("Jupiter", 6e24, 71000000, 'orange', 780597870700, 0, 0, 8760*1.8, can)

system = [terre, venus, soleil, mercure, mars, jupiter]

#main
can.pack()
deplacement()
root.mainloop()

