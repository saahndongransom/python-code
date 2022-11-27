
#Source code of Python Program to print remainder and quotient
def Solve(x, y):
    r = x % y
    q = x//y
    return (r, q)
try:
    x = int (input("Enter the first number:"))
    y = int (input("Enter the second number:"))
    r, q = Solve(x, y)
    print ("The remainder is ", r)
    print ("The quotient is ", q)
except:
    print ("Enter numeric value")