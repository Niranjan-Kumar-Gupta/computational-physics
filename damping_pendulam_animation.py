from visual import*
from visual.graph import *


display(width=600,height=600,center=vector(0,6,0))

base=box(pos=vector(0,-3.5,-1.6),size=vector(8,1.2,6),material=materials.wood)
wall=box(pos=vector(0,3.5,-1.8),size=vector(2.5,15,1),material=materials.wood)


bob=sphere(pos=vector(5,2,0),velocity=vector(0,0,0),radius=0.5,mass=5.0,color=color.red,material=materials.emissive)
pivot = vector(0,10,0) #point where attached
axle = cylinder(pos=pivot, axis=(0,0,-1.1), radius=0.3,material=materials.wood)
rod = cylinder(pos=pivot, axis=bob.pos-pivot, radius=0.03)

#Graph-------------------------------------------------------------------------------------------------
gdisplay(xtitle="time",ytitle="position",background=color.white,foreground=color.black)
ball=gcurve(color=color.red)


g=9.8
t=0
dt=0.01
ln = mag(bob.pos-pivot)
an = (ln-bob.pos.y)/ln
b=0.021
th=acos(an)
omega = 0.0

while(True):
    rate(100)

    acc = -g/ln*sin(th) - b*ln*omega
    th = th + omega*dt
    omega = omega+acc*dt
    bob.pos=vector(ln*sin(th),ln*(1-cos(th)),0)
    rod.axis = bob.pos-rod.pos
    ball.plot(pos=(t,bob.pos.x))
    t = t+dt
    
