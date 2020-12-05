print("Enter values n")
a=float(input("f(a)    = "))
b=float(input("del1f(a)= "))
c=float(input("del2f(a)= "))
d=float(input("del3f(a)= "))
e=float(input("del4f(a)= "))
g=float(input("del5f(a)= "))
h=float(input("del6f(a)= "))
i=float(input("del7f(a)= "))
u=float(input("u      = "))

x=a+u*b+u*(u-1)*c/2+u*(u-1)*(u-2)*d/6+u*(u-1)*(u-2)*(u-3)*e/24+u*(u-1)*(u-2)*(u-3)*(u-4)*g/120+u*(u-1)*(u-2)*(u-3)*(u-4)*(u-5)*h/120+u*(u-1)*(u-2)*(u-3)*(u-4)*(u-5)*(u-6)*i/720

print("Your required answer is : ",x)
