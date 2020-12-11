print("Enter values :")
a=float(input("y0    = "))
b=float(input("dely0= "))
c=float(input("dely-1= "))
d=float(input("del2y-1= "))
e=float(input("del3y-1= "))
f=float(input("del3y-2= "))
g=float(input("del4y-2= "))
u=float(input("u      = "))

x=a+u*(b+c)/2+u*u*d/2+u*(u*u*-1)*(e+f)/12+u*u*(u*u-1)*g/24

print("Your required answer is : ",x)
