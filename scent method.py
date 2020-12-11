
import numpy as np
print("\n---------------scecent  METHOD---------------\n")
print("f(x) = x^2 - 3")
def f(x):
    y = x**2 - 2.149
    return y
x1 = float(input("Enter the first guess value: "))
x2 = float(input("Enter the second guess value: "))
print("%-12s%-10s%-11s%-13s%-15s%-30s%-21s%-23s%-25s"% \
     ('Itration','x(left)','x(right)', 'f(x(left))','f(x(right))','x(i+1)=(x(left)+x(right))/2','f(x(i+1))','f(left)*f(right)','Error'))
m = f(x1) * f(x2)
n = f(x1) * f(x2)
error = 10E-3
itration=1
while(1):
    if(m<0):
        x3 = x2 - f(x2)*(x2-x1)/(f(x2)-f(x1))
        e = np.abs(x3-x1)
        print("%-12d%-10.5f%-11.5f%-13f%-15f%-30f%-21f%-23f%-25f"%(itration,x1,x2,f(x1),f(x2),x3,f(x3),n,e))
        if(error >= e):
            print("\nthe solution is %.5f "%x3)
            break
        n = f(x1) * f(x3)
        if(n<0.0):
            x2 = x3
        else:
            x1 = x3
        itration += 1

