import numpy as np
print("\n---------------NEWTON ROPHSON METHOD---------------\n")
print("f(x) = x^2 - 3")
print("f'(x) = 2*x\n")
def f(x):
    y = x**2 - 2.149
    return y
def f_dash(x):
    y = 2*x
    return y
x1 = float(input("Enter the guess value: "))
print()
print("%-12s%-10s%-11s%-13s%-15s%-15s"% \
     ('Itration','x(i)','x(i+1)','f(i)',"f'(i)",'Error'))

error = 10E-5
itration=1
while(1):
    x2 = x1 - f(x1)/f_dash(x1)
    e = np.abs(x2-x1)

    if(error >= e):
            print("\nthe solution is %.5f "%x2)
            break
    else:

        x1 = x2
    print("%-12d%-10.5f%-11.5f%-13f%-15f%-15f" % (itration, x1, x2, f(x1), f_dash(x1), e))
    itration += 1




