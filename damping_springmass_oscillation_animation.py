from visual import*
from visual.graph import *

scene.width = 1224
scene.height = 968
scene.title = "springmass_oscilation"
scene.forward = (-5,-.3,-1)
display(center=vector(7,0,-3))

wall=box(pos=vector(0,1,0),size=vector(0.2,3,2),color=vector(0.6,0.3,0.4))
floor=box(pos=vector(6,-0.6,0),size=vector(14,0.2,4),color=vector(0.6,0.3,0.4))
Mass=sphere(pos=vector(12,0,0),velocity=vector(0,0,0),radius=0.5,mass=5.0,color=color.red)
pivot = vector(0,0,0)
spring=helix(pos=pivot,axis=Mass.pos-pivot,radius=0.3,constant=1,thickness=0.1,coils=20)

b = 0.06
eq=vector(7,0,0)
t=0

dt=0.023

#Graph------------------------------------------------------
gdisplay(xtitle="time",ytitle="position",background=color.white,foreground=color.black)
ball=gcurve(color=color.red)



while (True):
    rate(100)    
    ball.plot(pos=(t,Mass.pos.x))
        
    acc=(eq-Mass.pos)*(spring.constant/Mass.mass)-b*Mass.velocity
        
    Mass.velocity = Mass.velocity + acc*dt
    Mass.pos = Mass.pos + Mass.velocity*dt
    spring.axis = Mass.pos-spring.pos
    t=t+dt
    
    

  
