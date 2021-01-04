#modules
from math import *
from tkinter import *
from random import *


#Constants
H = 1050
W = 1050 
G = 6.67430e-11

#planet class
class Planet:
    def __init__(self, name, mass, radius, color, x, y, vx, vy):
        """planets have coordinates in a fixed inertial frame"""
        self.name = name
        self.mass = mass
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        
        
    def accelerate(self, dt, a):
        """make the planet accelerate according to a acceleration vector a=(ax, ay)"""
        ax, ay = a
        self.vx = self.vx+ax*dt
        self.vy = self.vy+ay*dt

    def move(self, dt):
        """make the planet move according to its velocity vector """
        self.x = self.x+self.vx*dt
        self.y = self.y+self.vy*dt
        
    def field(self,x,y):
        """returns the gravitationnal field of the planet""" 
        d = sqrt((x-self.x)**2+(y-self.y)**2)
        if d==0:
            return 0,0
        gx = -(x-self.x)*G*self.mass/d**3
        gy = -(y-self.y)*G*self.mass/d**3
        return gx, gy


#planetary system class (also a tk canvas) 
class System(Canvas):
    def __init__(self, root, h, w, back, p_ref):
        Canvas.__init__(self, root, height = h, width = w, bg = back)
        self.planet_list = []
        self.picture = {}
        self.p_ref = p_ref
        self.centerx = 0
        self.centery = 0
        self.dt = 3600
        self.bind('<MouseWheel>', self.global_zoom)
        self.bind('<Button-1>', self.move_frame)
        self.bind('<Button-2>', self.reset_global_zoom)
        self.bind('<Button-3>', self.reset_frame)
        self.bind('<Shift-MouseWheel>', self.planet_zoom)
        self.bind('<Shift-Button-2>', self.reset_planet_zoom)
        self.grid(row = 0, column = 0, rowspan = 80)
        self.global_scale = 1/6400000000
        self.planet_scale = 1
        self.background_star_list = []
            
    def create_background_stars(self):
        color = ['red', 'orange', 'yellow', 'white', 'SteelBlue1', 'blue']
        for i in range(1000):
            x = randint(0, W)
            y = randint(0, H)
            star = self.create_oval(x,y,x+1,y+1, fill=choice(color))
            self.tag_lower(star)
            self.background_star_list.append(star)
            

    def delete_background_stars(self):
        for bgs in self.background_star_list:
            self.delete(bgs)
        self.background_star_list = []

    def create_planet(self, p):
        self.planet_list.append(p)
        x = p.x
        y = p.y
        radius = p.radius
        gs = self.global_scale = 1/6400000000
        ps = self.planet_scale = 1
        self.picture[p]=self.create_oval(W/2+(x-radius*ps)*gs, H/2+(y-radius*ps)*gs,W/2+(x+radius*ps)*gs, H/2+(y+radius*ps)*gs, fill = p.color)

    
    def field(self,x,y):
        """return the gravitational fied of the system"""
        gx = 0
        gy = 0
        for p in self.planet_list:
            gx+=p.field(x,y)[0]
            gy+=p.field(x,y)[1]
        return gx,gy

    def move(self):
        """move each planet in the system according to its field"""
        gs = self.global_scale
        ps = self.planet_scale
        for p in self.planet_list:
            p.accelerate(self.dt, self.field(p.x,p.y))
        for p in self.planet_list:
            p.move(self.dt)
            self.coords(self.picture[p], W/2+(p.x-p.radius*ps)*gs, H/2+(p.y-p.radius*ps)*gs,W/2+(p.x+p.radius*ps)*gs, H/2+(p.y+p.radius*ps)*gs)    
        for p in self.planet_list:
            Canvas.move(self,self.picture[p], -self.p_ref.x*gs-self.centerx, -self.p_ref.y*gs-self.centery)


    def move_frame(self, event):
        self.centerx += event.x-W/2
        self.centery += event.y-H/2

    def reset_frame(self, event):
        self.centerx = 0
        self.centery = 0

    def global_zoom(self, event):
        if event.delta>0:
            self.global_scale *=1.5
        else:
            self.global_scale /=1.5

    def reset_global_zoom(self, event):
        self.global_scale = 1/6400000000

    def planet_zoom(self, event):
        if event.delta>0:
            self.planet_scale *=1.5
        else:
            self.planet_scale /=1.5

    def reset_planet_zoom(self, event):
        self.planet_scale = 1




#parameters (also a tk frame)
class Parameters(Frame):
    def __init__(self, root, h, w, bg, system):
        Canvas.__init__(self, root, height = h, width = w, bg= bg)
        self.system = system
        
        #tk variables
        self.dt = IntVar()
        self.dt.set(3600)
        self.bgs = IntVar()
        self.bgs.set(0)
        
        #tk widgets
        self.dt_entry = Entry(root, textvariable=self.dt, width=30)
        self.dt_button = Button(root, text="OK", command=self.dt_get)
        self.p_ref_list = Listbox(root)
        for i in range(len(system.planet_list)):
            self.p_ref_list.insert(i+1, system.planet_list[i].name)
        self.bgs_box = Checkbutton(root, text="Background stars", variable=self.bgs)

        #tk labels
        Label(text = "Unit of time (s):").grid(row = 0, column = 1)
        Label(text = "Planet Frame:").grid(row = 5, column = 1)

        #tk labels and positionning
        self.dt_entry.grid(row = 1, column = 1)
        self.dt_button.grid(row = 2, column = 1)
        self.p_ref_list.grid(row = 6, column = 1)
        self.bgs_box.grid(row=8, column = 1)

        #binding
        self.p_ref_list.bind('<ButtonRelease-1>',self.p_ref_get)
        self.bgs_box.bind('<ButtonRelease-1>',self.bgs_get)
        


    def p_ref_get(self, event):
        i=self.p_ref_list.curselection()
        name = self.p_ref_list.get(i)
        for p in self.system.planet_list:
            if p.name==name:
                self.system.p_ref = p
                break

    def bgs_get(self, event):
        b = int(self.bgs.get())
        if b == 0:
            self.system.create_background_stars()
        else:
            self.system.delete_background_stars()
            
    def dt_get(self):
        self.system.dt = int(self.dt_entry.get())


