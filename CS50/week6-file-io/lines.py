import sys

#Verifies if the user inputs exactly one command-line arguments
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

filename = sys.argv[1]
if not filename.endswith(".py"):
    sys.exit("Not a Python file")

#Counts, excluding blank lines and comments, the amount of lines
try:
    with open(filename) as file:
        counter = 0
        for row in file:
            row = row.strip()
            if row and not row.startswith("#"):
                counter += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(counter)
