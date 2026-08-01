# converting string to datetime 

from datetime import datetime

date = datetime.strptime("06-07-2036", "%d-%m-%Y")
print(date)
date1 = datetime.strptime("2036-07-06", "%Y-%m-%d")
print(date1)

