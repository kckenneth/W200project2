#!/path/to/interpreter	
#!/usr/bin/env python

gallon_number=float(input("Enter a number of gallons of gasoline: "))
print("You entered the number of gallons of gasoline: ", gallon_number)
print("Equivalent number of liters: ", gallon_number*3.7854)
print("Number of barrels of oil required to produce it: ", gallon_number/19.5)
print("Price in U.S. dollars: {:.2f}".format(gallon_number*3.65))
