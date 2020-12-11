#Newton Forward
print("Enter values : ")
a=float(input("f(a)    = "))
b=float(input("del1f(a)= "))
c=float(input("del2f(a)= "))
d=float(input("del3f(a)= "))
e=float(input("del4f(a)= "))
z=float(input("f(a-)   = "))
#Newton Backward
g=float(input("neb1f(a)= "))
h=float(input("neb2f(a)= "))
i=float(input("neb3f(a)= "))
j=float(input("neb4f(a)= "))
#Gauss Forward
f=float(input("y0    = "))
k=float(input("dely0= "))
o=float(input("del2y-1= "))
s=float(input("del4y-2= "))
#Gauss Backward
l=float(input("dely-1= "))
q=float(input("del3y-2= "))
#Striling
p=float(input("del3y-1= "))
#Bressels
n=float(input("y1= "))
m=float(input("del2y0= "))
r=float(input("del4y-1= "))
u=float(input("u      = "))
v=float(input("v as u = "))

nf=a+u*b+u*(u-1)*c/2+u*(u-1)*(u-2)*d/6+u*(u-1)*(u-2)*(u-3)*e/24
nb=z+v*g+v*(v+1)*h/2+v*(v+1)*(v+2)*i/6+v*(v+1)*(v+2)*(v+3)*j/24
gf=f+u*k+u*(u-1)*o/2+(u+1)*u*(u-1)*p/6+(u+1)*u*(u-1)*(u-2)*s/24
gb=f+u*l+u*(u+1)*o/2+(u-1)*u*(u+1)*q/6+(u-1)*u*(u+1)*(u+2)*s/24
sf=f+u*(k+l)/2+u*u*o/2+u*(u*u*-1)*(p+q)/12+u*u*(u*u-1)*s/24
bs=(f+n)/2+(u-1/2)*k+u*(u-1)*(m+o)/4+(u-1/2)*u*(u-1)*p/6+(u+1)*u*(u-1)*(u-2)*(r+s)/48

print("Newton Forward is : ",nf)
print("Newton Backward is : ",nb)
print("Gauss Forward is : ",gf)
print("Gauss Backward is : ",gb)
print("Striling is : ",sf)
print("Bressel is : ",bs)
