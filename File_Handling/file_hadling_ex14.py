import os ,csv

rows = [["name","marks"],["Asha",88],["Ravi",89]]
with open ("student.csv","w",newline= "")as f :
    writer = csv.writer(f)
    writer.writerows(rows)



with open("student.csv", "r", newline="") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)