print("Enter values:")
a=float(input("f(a)    = "))
b=float(input("neb1f(a)= "))
c=float(input("neb2f(a)= "))
d=float(input("neb3f(a)= "))
e=float(input("neb4f(a)= "))
g=float(input("neb5f(a)= "))
h=float(input("neb6f(a)= "))
i=float(input("neb7f(a)= "))
u=float(input("u      = "))

x=a+u*b+u*(u+1)*c/2+u*(u+1)*(u+2)*d/6+u*(u+1)*(u+2)*(u+3)*e/24+u*(u+1)*(u+2)*(u+3)*(u+4)*g/120+u*(u+1)*(u+2)*(u+3)*(u+4)*(u+5)*h/120+u*(u+1)*(u+2)*(u+3)*(u+4)*(u+5)*(u+6)*i/720

print("Your required answer is : ",x)
