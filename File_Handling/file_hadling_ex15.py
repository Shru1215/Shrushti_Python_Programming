
import csv , os 

with open("students2.csv", "w", newline="") as f:
    fieldnames = ["name", "marks"]

    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({"name": "Asha", "marks": 88})
    writer.writerow({"name": "Ravi", "marks": 89})
    writer.writerow({"name": "Sita", "marks": 95})