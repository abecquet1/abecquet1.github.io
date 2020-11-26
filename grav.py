from math import *
from tkinter import *
from random import *

#Constants
H = 1050
W = 1680
GLOBAL_SCALE = 1/6400000000
PLANET_SCALE = 300
SLEEP = 1
VERBOSE = True
G = 6.67430e-11
DT = 36000
BACKGROUND_STARS = True

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
        self.picture = can.create_oval(W/2+(x-radius)*GLOBAL_SCALE, H/2+(y-radius)*GLOBAL_SCALE,W/2+(x+radius)*GLOBAL_SCALE, H/2+(y+radius)*GLOBAL_SCALE, fill = color)
        if VERBOSE:
            self.text = can.create_text(W/2+(x+radius)*GLOBAL_SCALE, H/2+(y+radius)*GLOBAL_SCALE, text=name, fill = 'gray')
        
    def accelerate(self, dt, a):
        """make the planet accelerate according to a acceleration vector a=(ax, ay)"""
        ax, ay = a
        self.vx = self.vx+ax*dt
        self.vy = self.vy+ay*dt

    def move(self, dt):
        """make the planet move according to its velocity vector """
        self.x = self.x+self.vx*dt
        self.y = self.y+self.vy*dt
        self.can.coords(self.picture, W/2+(self.x-self.radius)*GLOBAL_SCALE, H/2+(self.y-self.radius)*GLOBAL_SCALE,W/2+(self.x+self.radius)*GLOBAL_SCALE, H/2+(self.y+self.radius)*GLOBAL_SCALE)
        if VERBOSE:
            self.can.coords(self.text, W/2+(self.x+self.radius)*GLOBAL_SCALE, H/2+(self.y+self.radius)*GLOBAL_SCALE)
        
        #self.can.move(self.picture, self.vx*dt*GLOBAL_SCALE, self.vy*dt*GLOBAL_SCALE)
        
    def field(self,x,y):
        """returns the gravitationnal field of the planet""" 
        d = sqrt((x-self.x)**2+(y-self.y)**2)
        if d==0:
            return 0,0
        gx = -(x-self.x)*G*self.mass/d**3
        gy = -(y-self.y)*G*self.mass/d**3
        return gx, gy


class System:
    def __init__(self, planet_list, p_ref, can):
        self.planet_list = planet_list
        self.p_ref = p_ref
        self.can = can

    def field(self,x,y):
        """return the gravitational fieds of the system"""
        gx = 0
        gy = 0
        for p in self.planet_list:
            gx+=p.field(x,y)[0]
            gy+=p.field(x,y)[1]
        return gx,gy

    def move(self, dt):
        """move each planet in the system according to its field""" 
        for p in self.planet_list:
            p.accelerate(dt, self.field(p.x,p.y))
        for p in self.planet_list:
            p.move(dt)
        for p in self.planet_list:
            p.can.move(p.picture, -self.p_ref.x*GLOBAL_SCALE, -self.p_ref.y*GLOBAL_SCALE)
            p.can.move(p.text, -self.p_ref.x*GLOBAL_SCALE, -self.p_ref.y*GLOBAL_SCALE)




#Tkinter initialisation
root = Tk()
root.title("Gravitation")
can = Canvas(root, height = H, width = W, bg= 'black')

if BACKGROUND_STARS:
    color = ['red', 'orange', 'yellow', 'white', 'SteelBlue1', 'blue']
    for i in range(1000):
        x = randint(0, W)
        y = randint(0, H)
        can.create_oval(x,y,x+1,y+1, fill=choice(color))


#planets creation


sun = Planet("Sun", 2e30, 696342000*PLANET_SCALE, 'yellow', 0,0,0,0, can)
mercury = Planet("Mercury", 3e23, 2439000*PLANET_SCALE, 'gainsboro', 50597870700, 0,0,47362,can)
venus = Planet("Venus", 5e24, 6000000*PLANET_SCALE, 'floral white', 108000000000,0,0,35025, can)
earth = Planet("Earth", 6e24, 6400000*PLANET_SCALE, 'RoyalBlue4', 149597870700, 0, 0, 29783, can)
#moon = Planet("Moon", 7e22, 1700000*PLANET_SCALE, 'blue', 149597870700+380000000, 0, 0, 29783+1022, can)
mars = Planet("Mars", 6e23, 3400000*PLANET_SCALE, 'coral', -230655000000,0,0,-24080, can)
jupiter = Planet("Jupiter", 1.9e27, 71000000*PLANET_SCALE, 'burlywood3', 780597870700, 0, 0, 13058, can)
saturn = Planet("Saturn", 568e24, 60268000*PLANET_SCALE, 'khaki2', 1475500000000, 0, 0, 9640, can)
uranus = Planet("Uranus", 8.7e25, 25559000*PLANET_SCALE, 'DarkSlateGray1',   3008000000000, 0, 0, 6800, can)
neptune = Planet("Neptune", 1e26, 24764000*PLANET_SCALE, 'SkyBlue3',   4500000000000, 0, 0, 5430, can)


solar_system = System([sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune], earth, can)




#main
def deplacement(): 
    solar_system.move(DT)    
    root.after(SLEEP,deplacement)

can.pack()
deplacement()
root.mainloop()



