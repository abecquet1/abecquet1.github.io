from math import *
from tkinter import *
from random import *



#Constants
H = 1050
W = H#1680
GLOBAL_SCALE = 1/6400000000
PLANET_SCALE = 1
SLEEP = 1
VERBOSE = False
G = 6.67430e-11
DT = 3600 #3600s = 1h
BACKGROUND_STARS = False



#Planet class
class Planet:
    def __init__(self, name, mass, radius, color, x, y, vx, vy, can):
        """planets have coordinates in a fixed inertial frame"""
        self.name = name
        self.mass = mass
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.can = can
        self.picture = can.create_oval(W/2+(x-radius*PLANET_SCALE)*GLOBAL_SCALE, H/2+(y-radius*PLANET_SCALE)*GLOBAL_SCALE,W/2+(x+radius*PLANET_SCALE)*GLOBAL_SCALE, H/2+(y+radius*PLANET_SCALE)*GLOBAL_SCALE, fill = color)
        if VERBOSE:
            self.text = can.create_text(W/2+(x+radius*PLANET_SCALE)*GLOBAL_SCALE, H/2+(y+radius*PLANET_SCALE)*GLOBAL_SCALE, text=name, fill = 'gray')
        
    def accelerate(self, dt, a):
        """make the planet accelerate according to a acceleration vector a=(ax, ay)"""
        ax, ay = a
        self.vx = self.vx+ax*dt
        self.vy = self.vy+ay*dt

    def move(self, dt):
        """make the planet move according to its velocity vector """
        self.x = self.x+self.vx*dt
        self.y = self.y+self.vy*dt
        self.can.coords(self.picture, W/2+(self.x-self.radius*PLANET_SCALE)*GLOBAL_SCALE, H/2+(self.y-self.radius*PLANET_SCALE)*GLOBAL_SCALE,W/2+(self.x+self.radius*PLANET_SCALE)*GLOBAL_SCALE, H/2+(self.y+self.radius*PLANET_SCALE)*GLOBAL_SCALE)
        if VERBOSE:
            self.can.coords(self.text, W/2+(self.x+self.radius*PLANET_SCALE)*GLOBAL_SCALE, H/2+(self.y+self.radius*PLANET_SCALE)*GLOBAL_SCALE)
        
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
        self.centerx = 0
        self.centery = 0
        self.can = can

    def field(self,x,y):
        """return the gravitational fied of the system"""
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
            p.can.move(p.picture, -self.p_ref.x*GLOBAL_SCALE-self.centerx, -self.p_ref.y*GLOBAL_SCALE-self.centery)
            if VERBOSE:
                p.can.move(p.text, -self.p_ref.x*GLOBAL_SCALE-self.centerx, -self.p_ref.y*GLOBAL_SCALE-self.centery)



#Tkinter initialisation and bindings
root = Tk()
root.title("Gravitation")
can = Canvas(root, height = H, width = W, bg= 'black')


if BACKGROUND_STARS:
    color = ['red', 'orange', 'yellow', 'white', 'SteelBlue1', 'blue']
    for i in range(1000):
        x = randint(0, W)
        y = randint(0, H)
        can.create_oval(x,y,x+1,y+1, fill=choice(color))

def move_frame(event):
    solar_system.centerx += event.x-W/2
    solar_system.centery += event.y-H/2

def reset_frame(event):
    solar_system.centerx = 0
    solar_system.centery = 0

def global_zoom(event):
    global GLOBAL_SCALE
    if event.delta>0:
        GLOBAL_SCALE *=1.5
    else:
        GLOBAL_SCALE /=1.5

def reset_global_zoom(event):
    global GLOBAL_SCALE
    GLOBAL_SCALE = 1/6400000000

def planet_zoom(event):
    global PLANET_SCALE
    if event.delta>0:
        PLANET_SCALE *=1.5
    else:
        PLANET_SCALE /=1.5

def reset_planet_zoom(event):
    
    global PLANET_SCALE
    PLANET_SCALE = 1
            
can.bind('<MouseWheel>', global_zoom)
can.bind('<Button-1>', move_frame)
can.bind('<Button-2>', reset_global_zoom)
can.bind('<Button-3>', reset_frame)
can.bind('<Shift-MouseWheel>', planet_zoom)
can.bind('<Shift-Button-2>', reset_planet_zoom)



#planets and system creation
sun = Planet("Sun", 2e30, 696342000, 'yellow', 0,0,0,0, can)
mercury = Planet("Mercury", 3e23, 2439000, 'gainsboro', 50597870700, 0,0,47362,can)
venus = Planet("Venus", 5e24, 6000000, 'floral white', 108000000000,0,0,35025, can)
earth = Planet("Earth", 6e24, 6400000, 'RoyalBlue4', 149597870700, 0, 0, 29783, can)
moon = Planet("Moon", 7e22, 1700000, 'grey', 149597870700+380000000, 0, 0, 29783+1022, can)
mars = Planet("Mars", 6e23, 3400000, 'coral', -230655000000,0,0,-24080, can)
jupiter = Planet("Jupiter", 1.9e27, 71000000, 'burlywood3', 780597870700, 0, 0, 13058, can)
saturn = Planet("Saturn", 568e24, 60268000, 'khaki2', 1475500000000, 0, 0, 9640, can)
uranus = Planet("Uranus", 8.7e25, 25559000, 'DarkSlateGray1',   3008000000000, 0, 0, 6800, can)
neptune = Planet("Neptune", 1e26, 24764000, 'SkyBlue3',   4500000000000, 0, 0, 5430, can)

solar_system = System([sun, mercury, venus, earth, moon, mars, jupiter, saturn, uranus, neptune], sun, can)



#main
def deplacement(): 
    solar_system.move(DT)    
    root.after(SLEEP,deplacement)



liste = Listbox(root)
for i in range(len(solar_system.planet_list)):
    liste.insert(i+1, solar_system.planet_list[i].name)

def clic_liste(event):
    i=liste.curselection()
    name = liste.get(i)
    for p in solar_system.planet_list:
        if p.name==name:
            solar_system.p_ref = p
            break

    
liste.bind('<ButtonRelease-1>',clic_liste)


def recupere():
    global DT
    DT = int(entree.get())

value = IntVar() 
value.set(3600)
entree = Entry(root, textvariable=value, width=30)

bouton = Button(root, text="Valider", command=recupere)


can.grid(row = 0, column = 0, rowspan = 80)
Label(text = "Unit of time (s):").grid(row = 0, column = 1)
entree.grid(row = 1, column = 1)
bouton.grid(row = 2, column = 1)

Label(text = "Planet Frame:").grid(row = 5, column = 1)
liste.grid(row = 6, column = 1)


deplacement()
root.mainloop()



