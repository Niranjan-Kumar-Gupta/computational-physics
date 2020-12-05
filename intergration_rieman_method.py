from visual import*
from visual.graph import*



def function(x):
    f=x
    return f

lower_limit=0
upper_limit=1
dx=0.0001
intergal=0
x=lower_limit
while(x<=upper_limit):
    area=function(x)*dx
    intergal=intergal+area
    x=x+dx
print(intergal)    
    
