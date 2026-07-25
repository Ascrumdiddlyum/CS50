import sys
import csv
from tabulate import tabulate

#Verifies if there is exactly one command-line argument
def verify(argument):
    if len(argument) > 2:
        sys.exit("Too many command-line arguments")
    if len(argument)< 2:
        sys.exit("Too few command-line arguments")

#Tabulates the inputted CSV file
def print_table(argument):
    try:
        with open(f"data/pizza/{argument[1]}") as file:
            reader = csv.reader(file)
            headers = next(reader)
            table = list(reader)
    except FileNotFoundError:
        sys.exit("File doesn't exist")
    print(tabulate(table, headers, tablefmt="grid"))

verify(sys.argv)
tabulate(sys.argv)