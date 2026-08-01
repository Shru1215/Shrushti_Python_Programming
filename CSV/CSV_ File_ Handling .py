#Write student data into student.csv.
#
# write
import os ,csv
rows = [["Name","Marks"],["Asha",88],["ravi",89],["sita",100]]
with open("student.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# write

with open("student.csv", "r", newline="") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)


#Write only one row
with open("student.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["Name", "Marks"])
    writer.writerow(["Asha", 88])

#Read only the header

with open("student.csv", "r") as f:
    reader = csv.reader(f)

    header = next(reader)    # reads only header (header)
    print(header)

#Print only student names

with open("student.csv", "r") as f:
    reader = csv.reader(f)

    next(reader)

    for row in reader:
        print(row[0])

# Print only student marks

with open("student.csv", "r") as f:
    reader = csv.reader(f)

    next(reader)

    for row in reader:
        print(row[1])


# use DictWriter
with open("student.csv", "w", newline="") as f:

    fieldnames = ["Name", "Marks"]

    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({"Name": "Asha", "Marks": 88})
    writer.writerow({"Name": "Ravi", "Marks": 89})

#Use DictReader
with open("student.csv", "r") as f:

    reader = csv.DictReader(f)

    for row in reader:
        print(row)

# 

with open("student.csv", "r") as f:

    reader = csv.DictReader(f)

    for row in reader:
        if int(row["Marks"]) > 88:
            print(row["Name"], row["Marks"])

#Add a new student (Append)
with open("student.csv", "a", newline="") as f:

    writer = csv.writer(f)

    writer.writerow(["Ram", 91])