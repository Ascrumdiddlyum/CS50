import sys
import csv
from tabulate import tabulate

#Verifies if there is exactly one command-line argument
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv)< 2:
    sys.exit("Too few command-line arguments")

#Tabulates the inputted CSV file
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            headers = next(reader)
            table = list(reader)
except FileNotFoundError:
    sys.exit("File doesn't exist")

print(tabulate(table, headers, tablefmt="grid"))
