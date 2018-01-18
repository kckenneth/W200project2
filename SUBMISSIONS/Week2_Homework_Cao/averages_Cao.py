import math
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
option=str(input("Enter a type of average out of the three options: arithmetic, geometric, or root-mean-square: "))
if option=="arithmetic":
    average=(a+b)/2
    print("The arithmetic mean is: ", average)
elif option=="geometric":
    average=math.sqrt(a*b)
    print("The geometric mean is: ", average)
elif option=="root-mean-square":
    average=math.sqrt((a**2+b**2)/2)
    print("The root-mean-square is : ", average)
else:
    print("You entered an invalid option")

