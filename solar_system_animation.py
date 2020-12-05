from visual import*
from visual.graph import*
#from numpy import*
#P_graph=gcurve(color=color.red)
display()
scene.center
def g_force(p1,p2):
    G=1
    r_vec=p1.pos-p2.pos
    r_mag=mag(r_vec)
    r_unit=r_vec/r_mag
    force_mag=G*p1.mass*p2.mass/r_mag**2
    force_vec=-force_mag*r_unit
    return force_vec
sun=sphere(pos=vector(0,0,0),radius=0.2,color=color.orange,mass=550,momentum=vector(0,0,0),make_trail=True)
earth=sphere(pos=vector(1.05,0,0),radius=0.05,color=vector(0.3,0.2,0.6),mass=1.05,momentum=vector(0,30,0),make_trail=True)
p1=sphere(pos=vector(-2,0,0),radius=0.075,color=color.red,mass=2,momentum=vector(0,-35,0),make_trail=True)
p2=sphere(pos=vector(1.5,0,0),radius=0.1,color=vector(0.3,0.5,0.2),mass=3,momentum=vector(0,40,0),make_trail=True)
dt=0.00001
t=0
while(True):
    rate(500000)
    sun.force=g_force(sun,earth)+g_force(sun,p1)+g_force(sun,p2)
    earth.force=g_force(earth,sun)+g_force(earth,p1)+g_force(earth,p2)
    p1.force=g_force(p1,sun)+g_force(p1,earth)+g_force(p1,p2)
    p2.force=g_force(p2,sun)+g_force(p2,earth)+g_force(p2,p1)
    sun.momentum=sun.momentum+sun.force*dt
    earth.momentum=earth.momentum+earth.force*dt
    p2.momentum=p2.momentum+p2.force*dt
    p1.momentum=p1.momentum+p1.force*dt
    sun.pos=sun.pos+sun.momentum/sun.mass*dt
    earth.pos=earth.pos+earth.momentum/earth.mass*dt
    p1.pos=p1.pos+p1.momentum/p1.mass*dt
    p2.pos=p2.pos+p2.momentum/p2.mass*dt
    t=t+dt
    
