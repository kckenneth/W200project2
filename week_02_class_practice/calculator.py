# Insert your code here
#!/path/to/interpreter	
#!/usr/bin/env python
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operator=str(input("Enter an operator: "))
if operator=="+":
    print(num1,"+",num2,"=",num1 + num2)
elif operator=="-":
    print(num1,"-",num2,"=",num1 - num2)
elif operator=="*":
    print(num1,"*",num2,"=",num1 * num2)
elif operator=="/":
    print(num1,"/",num2,"=",num1 / num2)
else:
    print("You picked an invalid operator.")
