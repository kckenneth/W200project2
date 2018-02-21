import sys

if len(sys.argv) == 2:
    rack = sys.argv[1].lower()
elif len(sys.argv) >3:
    rack = sys.argv[1].lower()
    loc = sys.argv[2]
    char = sys.argv[3].lower()
else:
    sys.exit("Error: You need to enter some letters without spaces for rack word, an integer for location and letter for the choice")

print(loc)
print(char)
