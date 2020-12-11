import numpy as np
print( " f(x) =  1/(5+4*cos(x))")
def f(x):
    y = 1/(x+6)
    return y
low = 1
up = 2
h=(up-low)/6
intergal = 0
print("%-10s%-11s"% \
     ('x(i)','f(i)'))

x=h
while(x<up-h):
    print("%-10.4s%-11.4s" % (x,f(x)))

    intergal += f(x)
    x=x+h

print(intergal*h + h*(f(low)+f(up))/2)