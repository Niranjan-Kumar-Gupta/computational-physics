print("Enter values :")
a=float(input("y0    = "))
b=float(input("dely0= "))
c=float(input("del2y-1= "))
d=float(input("del3y-1= "))
e=float(input("del4y-2= "))
u=float(input("u      = "))

x=a+u*b+u*(u-1)*c/2+(u+1)*u*(u-1)*d/6+(u+1)*u*(u-1)*(u-2)*e/24

print("Your required answer is : ",x)
