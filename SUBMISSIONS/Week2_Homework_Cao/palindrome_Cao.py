#!/path/to/interpreter	
#!/usr/bin/env python

name=str(input("Enter your name: "))
reversename=name[::-1]
reversename=reversename[0].upper() + reversename[1:].lower()
length=len(reversename)
count=0
while count<length:
    letter=reversename[count]
    print(letter,end='')
    count+=1
if name.lower()==reversename.lower():
    print("\nPalindrome!")
