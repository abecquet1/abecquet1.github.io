from grav import *

#MAIN

#Tkinter initialisation
root = Tk()
root.title("Gravitation")



p_list = []

f = open("ss.csv", 'r')
tab = f.readlines()
f.close()
for i in range(len(tab)):
    tab[i] = tab[i].split(',')


for i in range(1,51):
    name = tab[i][1]
    print("Adding "+name, end = ', ')
    mass = float(tab[i][4])
    radius = float(tab[i][3])*500
    if i not in [5,17,18,19,20,23,24,25,26,27,28,31,32,33,34,35,37,39]:
        a = float(tab[i][5])*149597870700
        x = float(tab[i][8])*149597870700
    else:
        a = float(tab[i][5])*1000000
        x = float(tab[i][8])*1000000
    y = 0
    color = tab[i][11]
    theta = random()*2*pi
    (x,y) = (x*cos(theta)-y*sin(theta), x*sin(theta)+y*cos(theta))
    if i == 5:
        i_ref = 3
    elif i in [17,18,19,20]:
        i_ref = 15
    elif i in [23,24,25,26,27,28]:
        i_ref = 21
    elif i in [31,32,33,34,35]:
        i_ref = 29
    elif i == 37:
        i_ref = 35
    elif i == 39:
        i_ref = 37
    else:
        i_ref = 0
        
        
    e = float(tab[i][9])
    vx = 0
    vy = 0
    if i != 1:
        print("satelite of "+p_list[i_ref].name)
        vy = sqrt((p_list[i_ref].mass+mass)*G*(1-e)/a/(1+e))
        (vx,vy) = (vx*cos(theta)-vy*sin(theta), vx*sin(theta)+vy*cos(theta))
        (vx,vy) = (p_list[i_ref].vx+vx, p_list[i_ref].vy+vy)
        (x,y) = (p_list[i_ref].x+x,p_list[i_ref].y+y)
    p_list.append(Planet(name,mass,radius,color, x, y,vx,vy))
    
    

#solar_system
solar_system = System(root, H, W, 'black',p_list[0])
solar_system.dt = 0

for p in p_list:
    solar_system.create_planet(p)

    
#parameters
parameters = Parameters(root, H, 630, 'gray', solar_system)

#mainloop
def deplacement(): 
    solar_system.move()    
    root.after(1,deplacement)

deplacement()
root.mainloop()


