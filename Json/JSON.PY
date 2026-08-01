#Store student details in student.json.

import json

student = {
    "name": "Asha",
    "marks": 88,
    "city": "Hubli"
}

with open("student.json", "w") as f:
    json.dump(student, f)

# read 
import json

with open("student.json", "r") as f:
    data = json.load(f)

print(data)

#Convert a dictionary to a JSON string

student = {
    "name": "Ravi",
    "marks": 90
}

result = json.dumps(student)

print(result)

#Print only the student's name

with open("student.json", "r") as f:
    data = json.load(f)

print(data["name"])

#Print all keys
import json

with open("student.json", "r") as f:
    data = json.load(f)

for key in data:
    print(key)

# print values

with open("student.json", "r") as f:
    data = json.load(f)

for value in data.values():
    print(value)

#update marks 

with open("student.json", "r") as f:
    data = json.load(f)

data["marks"] = 95

with open("student.json", "w") as f:
    json.dump(data, f)

# Add a new key
with open("student.json", "r") as f:
    data = json.load(f)

data["course"] = "Python"

with open("student.json", "w") as f:
    json.dump(data, f)


#Delete a key
with open("student.json", "r") as f:
    data = json.load(f)

del data["city"]

with open("student.json", "w") as f:
    json.dump(data, f)