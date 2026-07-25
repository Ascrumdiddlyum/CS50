import csv
import sys

def verify(argument):
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    for arg in argument[-2:]:
        if not arg.endswith(".csv"):
            sys.exit("Not a CSV file")

def rewrite_names(argument):
    try:
        with open(f"data/scourgify/{argument[1]}") as file:
            reader = csv.reader(file)
            next(reader)
            with open(f"data/scourgify/{argument[2]}", "w") as newfile:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(newfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    name, house = row
                    last, first = name.split(", ")
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {argument[1]}")

verify(sys.argv)
rewrite_names(sys.argv)

            

                
    

