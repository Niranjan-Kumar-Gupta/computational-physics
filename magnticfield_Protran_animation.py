from visual import*

scene.width = 1090
scene.height = 720
scene.title = "magntic field"
scene.forward = (0,-.1,-1)


qe = 1.6e-19
mp=1.9e-27
me=1e-7
B0=vector(0,0.2,0)
bscale=1

xmax=0.4
dx=0.1
yg=-0.1
x=-xmax

while(x<=xmax):
    curve(pos=[vector(x,yg,-xmax),vector(x,yg,xmax)],color=vector(0.7,0.7,0.7))
    x=x+dx
z=-xmax
while(z<=xmax):
    curve(pos=[vector(-xmax,yg,z),vector(xmax,yg,z)],color=vector(0.7,0.7,0.7))
    z=z+dx

x=-xmax
while(x<=xmax):
    z=-xmax
    while(z<=xmax):
        arrow(pos=vector(x,yg,z),axis=B0*bscale,color=color.cyan)
        z=z+dx
    x=x+dx    

rad=1.5e-2
proton=sphere(pos=vector(0.15,0.1,0),color=color.red,make_trail=True,material=materials.emissive,radius=rad,retain=20000,velocity=vector(0,0,-2e7))
#l1 = local_light(pos=proton.pos, color=proton.color)
lb_p = label( text="proton", xoffset=1.5e-2, yoffset=1.5e-2, pos=(0.15,0.1,0),opacity=0, box=0, line=0,m=mp,q=qe,v=proton.velocity)
lb_m = label( text="Magantic field", xoffset=3e-2, yoffset=3e-2, pos=(xmax,yg,-xmax),opacity=0, box=0, line=0)
dt=5e-11

while(True):
    rate(500)
    force=qe*cross(proton.velocity,B0)
    proton.velocity += force/mp*dt
    proton.pos += proton.velocity*dt
    force=lb_p.q*cross(lb_p.v,B0)
    lb_p.v += force/lb_p.m*dt
    lb_p.pos += lb_p.v*dt
    




    
