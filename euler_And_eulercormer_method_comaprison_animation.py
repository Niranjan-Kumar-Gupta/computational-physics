from visual import*
from visual.graph import *
scene.width = 1224
scene.height = 968
scene.title = "springmass_oscilation"
scene.forward = (0,-.3,-1)
display(center=vector(12,0,0))
wall=box(pos=vector(0,1,0),size=vector(0.2,3,2),color=vector(0.6,0.3,0.4))
floor=box(pos=vector(6,-0.6,0),size=vector(14,0.2,4),color=vector(0.6,0.3,0.4))
Mass=sphere(pos=vector(12,0,0),velocity=vector(0,0,0),radius=0.5,mass=5.0,color=color.red)
pivot = vector(0,0,0)
spring=helix(pos=pivot,axis=Mass.pos-pivot,radius=0.3,constant=1,thickness=0.1,coils=20)
Mass1=sphere(pos=vector(12,0,0),velocity=vector(0,0,0),radius=0.5,mass=5.0,color=color.red)
r=3
eq=vector(9,0,0)
t=0
m=0.5
dt=0.023
#Graph------------------------------------------------------
gdisplay(xtitle="time",ytitle="position",background=color.black,foreground=color.white)
ball=gcurve(color=color.cyan)
ball1=gcurve(color=color.yellow)
while (True):
    rate(100)    
    ball.plot(pos=(t,Mass.pos.x))       
    acc = (eq-Mass.pos)*(spring.constant/Mass.mass)    
    Mass.velocity = Mass.velocity+acc*dt
    Mass.pos = Mass.pos+Mass.velocity*dt
    spring.axis = Mass.pos-spring.pos
    acc1 = (eq-Mass1.pos)*(spring.constant/Mass1.mass)       
    Mass1.pos = Mass1.pos+Mass1.velocity*dt
    Mass1.velocity = Mass1.velocity+acc1*dt
    ball1.plot(pos=(t,Mass1.pos.x))   
    t=t+dt
