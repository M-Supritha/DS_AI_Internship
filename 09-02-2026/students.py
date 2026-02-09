import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    
    print("Students who Failed:")
    for row in reader:
        if row["Status"] == "Fail":
            print(row["Name"])
