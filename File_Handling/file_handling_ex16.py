import os , json
data = {"name:" "ravi","age:" "45","skils:" ["python","sql"]}

with open ("profile.json","w")as f :
    json.dump(data,f,indent = 2 )

with open ("profile.json","r") as f :
    loaded = json.load(f)
    print(loaded["skills"])