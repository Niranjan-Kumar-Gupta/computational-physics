print("Enter values :")
a=float(input("y0    = "))
b=float(input("y1= "))
c=float(input("dely0= "))
d=float(input("del2y0= "))
e=float(input("del2y-1= "))
f=float(input("del3y-1= "))
g=float(input("del4y-1= "))
h=float(input("del4y-2= "))
u=float(input("u      = "))

x=(a+b)/2+(u-1/2)*c+u*(u-1)*(d+e)/4+(u-1/2)*u*(u-1)*f/6+(u+1)*u*(u-1)*(u-2)*(g+h)/48

print("Your required answer is : ",x)
