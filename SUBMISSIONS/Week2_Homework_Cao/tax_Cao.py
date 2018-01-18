#!/path/to/interpreter	
#!/usr/bin/env python

income = int(input("Please enter your income:"))
if income<=1000 and income>=0:
    tax=income*0.05
    print("Tax owed: {:.2f}".format(tax))
elif income <=2000 and income>1000:
    tax=1000*0.05+(income-1000)*0.10
    print("Tax owed: {:.2f}".format(tax))
elif income > 2000:
    tax=1000*0.05+1000*0.10+(income-2000)*0.15
    print("Tax owed: {:.2f}".format(tax))
else:
    print("You entered an invalid income number")
