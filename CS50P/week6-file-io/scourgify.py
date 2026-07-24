import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    with open("before.csv") as file:
        reader = csv.reader(file)
        next(reader)
        with open(sys.argv[2], "w") as newfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(newfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                name, house = row
                last, first = name.split(", ")
                writer.writerow({"first": first, "last": last, "house": house})

except FileNotFoundError:
    sys.exit(f"Could not read{sys.argv[1]}")

            

                
    

